"""Offline checks for the Day 7 solution code (src/). Fake clients only test control
flow; they never measure retrieval or answer quality."""
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.agent import Agent, AgentConfig  # noqa: E402
from src.cli import coverage  # noqa: E402
from src.retrievers import BM25Retriever, HybridRetriever, check_filters, tokenize  # noqa: E402


def chunk(cid, page, text, ctype="text", chapter="ch3"):
    return {"id": cid, "text": text, "source_id": "doc", "source": "doc.pdf", "page": page,
            "metadata": {"document_id": "doc", "source": "doc.pdf", "page": page, "chapter": chapter,
                         "content_type": ctype, "printed_page": page - 1}}


CHUNKS = [chunk("c1", 10, "Màu bổ túc: cặp vàng và tím"),
          chunk("c2", 11, "Màu tương đồng nằm cạnh nhau trên vòng màu"),
          chunk("c3", 12, "Bảng phím tắt CTRL + J nhân đôi Layer", chapter="appendix")]


class FakeDense:
    name = "dense"

    def search(self, query, *, filters=None, top_k=5):
        rows = [c for c in CHUNKS if not filters or all(c["metadata"].get(k) == v for k, v in filters.items())]
        return [{**c, "score": 1.0 / (i + 1), "rank": i + 1, "method": "dense"} for i, c in enumerate(rows[::-1][:top_k])]


class RetrievalTests(unittest.TestCase):
    def test_tokenize_adds_syllable_bigrams(self):
        self.assertIn("màu_sắc", tokenize("Màu sắc"))

    def test_bm25_ranks_lexical_match_first_and_filters(self):
        bm = BM25Retriever(CHUNKS)
        self.assertEqual(bm.search("nhân đôi layer", top_k=3)[0]["id"], "c3")
        self.assertEqual(bm.search("nhân đôi layer", filters={"chapter": "ch3"}, top_k=3), [])

    def test_rrf_fuses_ranks_not_scores(self):
        hy = HybridRetriever(FakeDense(), BM25Retriever(CHUNKS), k=60, candidates=3)
        res = hy.search("cặp vàng và tím", top_k=3)
        self.assertEqual(len({r["id"] for r in res}), len(res))
        self.assertTrue(all("component_ranks" in r for r in res))

    def test_filter_whitelist(self):
        with self.assertRaises(ValueError):
            check_filters({"answer": "x"})

    def test_multihop_coverage_needs_every_group(self):
        q = {"gold": [{"source_id": "doc", "page": 10, "evidence": "vàng và tím", "group": "a"},
                      {"source_id": "doc", "page": 11, "evidence": "cạnh nhau", "group": "b"}]}
        self.assertFalse(coverage(q, CHUNKS[:1])["all"])
        self.assertTrue(coverage(q, CHUNKS[:2])["all"])


def tool_call(name, args, i):
    fn = SimpleNamespace(name=name, arguments=json.dumps(args, ensure_ascii=False))
    tc = SimpleNamespace(id=f"t{i}", function=fn)
    tc.model_dump = lambda: {"id": f"t{i}", "type": "function", "function": {"name": name, "arguments": fn.arguments}}
    return tc


class FakeClient:
    """Replays scripted tool calls like the OpenAI chat API."""

    def __init__(self, script):
        self.script = iter(script)
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self.create))

    def create(self, **kw):
        name, args = next(self.script)
        msg = SimpleNamespace(content=None, tool_calls=[tool_call(name, args, id(kw))])
        return SimpleNamespace(choices=[SimpleNamespace(message=msg)],
                               usage=SimpleNamespace(prompt_tokens=10, completion_tokens=5))


class AgentTests(unittest.TestCase):
    def run_agent(self, script, **cfg):
        agent = Agent(AgentConfig("t", **cfg), FakeDense(), CHUNKS, FakeClient(script))
        return agent.run("Màu bổ túc của tím?", "q1")

    def test_answer_with_valid_citation(self):
        r = self.run_agent([("search_docs", {"query": "bổ túc tím", "chapter": None, "content_type": None}),
                            ("final_answer", {"answer": "Vàng [c1]", "citations": ["c1"], "abstain": False})])
        self.assertEqual(r["status"], "answered")
        self.assertEqual(r["citations"], ["c1"])
        self.assertEqual(r["n_retrieval_calls"], 1)

    def test_citation_not_in_context_becomes_abstain(self):
        r = self.run_agent([("search_docs", {"query": "x", "chapter": "appendix", "content_type": None}),
                            ("final_answer", {"answer": "Vàng [c1]", "citations": ["c1"], "abstain": False})])
        self.assertEqual(r["status"], "abstain")
        self.assertTrue(any(e["event"] == "invalid_citations" for e in r["events"]))

    def test_budget_drops_chunks(self):
        r = self.run_agent([("search_docs", {"query": "x", "chapter": None, "content_type": None}),
                            ("final_answer", {"answer": "", "citations": [], "abstain": True})], budget=40)
        self.assertLessEqual(r["context_chars"], 40)
        self.assertTrue(r["events"][1]["dropped_ids"])

    def test_step_limit_forces_final(self):
        script = [("search_docs", {"query": str(i), "chapter": None, "content_type": None}) for i in range(2)]
        script.append(("final_answer", {"answer": "", "citations": [], "abstain": True}))
        r = self.run_agent(script, max_steps=2)
        self.assertEqual(r["status"], "abstain")
        self.assertEqual(r["n_retrieval_calls"], 2)
        self.assertTrue(any(e.get("forced_final") for e in r["events"]))

    def test_read_page_only_when_enabled(self):
        r = self.run_agent([("read_page", {"page": 10}),
                            ("final_answer", {"answer": "", "citations": [], "abstain": True})])
        self.assertTrue(any(e["event"] == "tool_error" for e in r["events"]))
        r = self.run_agent([("read_page", {"page": 10}),
                            ("final_answer", {"answer": "Vàng [c1]", "citations": ["c1"], "abstain": False})],
                           allow_read_page=True)
        self.assertEqual(r["status"], "answered")


if __name__ == "__main__":
    unittest.main()
