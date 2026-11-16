"""Day 7 command line. Run from the repo root.

    python -m src.cli export --collection colorme3_B4                 # Day 6 Chroma -> data/colorme_chunks_colorme3_B4.json
    python -m src.cli validate --collection colorme3_B4               # check benchmark evidence against chunks
    python -m src.cli retrieval --split dev --collection colorme3_B4  # Hit@1 / Evidence Hit@3 / MRR for every method
    python -m src.cli agent --config luna_v4_fb_b4 --split dev        # run the real agent, save traces
    python -m src.cli sheet --config luna_v4_fb_b4 --split test       # markdown sheet for manual labelling
    python -m src.cli score --config luna_v4_fb_b4 --split test       # aggregate manual labels (+ agent_metrics files)
Submitted configuration: luna_v4_fb_b4 (round 3).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import sys
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import config
from .agent import Agent, AgentConfig
from .retrievers import USAGE, Day6Store, build, load_chunks, openai_client

# Agent configurations compared on dev (fixed before running test; see report)
CONFIGS = {
    "dense": AgentConfig("dense", method="dense", top_k=5, notes="baseline: dense Day 6 index only"),
    "bm25": AgentConfig("bm25", method="bm25", top_k=5, notes="lexical BM25 (syllable uni+bigram)"),
    "hybrid": AgentConfig("hybrid", method="hybrid", top_k=5, notes="RRF(dense, BM25)"),
    "hybrid_page": AgentConfig("hybrid_page", method="hybrid", top_k=5, allow_read_page=True,
                               notes="improvement 1: + read_page tool (neighbour/whole-page context)"),
    "rerank_page": AgentConfig("rerank_page", method="rerank", top_k=5, allow_read_page=True,
                               notes="improvement 2: hybrid 15 candidates -> LLM rerank -> top5, + read_page"),
    "hybrid_page_strict": AgentConfig("hybrid_page_strict", method="hybrid", top_k=5, allow_read_page=True, prompt="v2",
                                      notes="improvement 3: hybrid_page + strict grounding prompt (dev error dv_tx3)"),
    "rerank_page_strict": AgentConfig("rerank_page_strict", method="rerank", top_k=5, allow_read_page=True, prompt="v2",
                                      notes="improvement 4: rerank_page + strict grounding prompt"),
    "dense_strict": AgentConfig("dense_strict", method="dense", top_k=5, prompt="v2",
                                notes="control: baseline dense + strict prompt (isolates prompt effect)"),
    "hybrid_page_strict_41": AgentConfig("hybrid_page_strict_41", method="hybrid", top_k=5, allow_read_page=True,
                                         prompt="v2", model="gpt-4.1",
                                         notes="improvement 5: hybrid_page_strict with gpt-4.1 controller"),
    "hybrid_page_verify": AgentConfig("hybrid_page_verify", method="hybrid", top_k=5, allow_read_page=True,
                                      prompt="v2", verify=True,
                                      notes="improvement 6: hybrid_page_strict + answer verifier (removes unsupported claims)"),
    "rerank_page_verify": AgentConfig("rerank_page_verify", method="rerank", top_k=5, allow_read_page=True,
                                      prompt="v2", verify=True,
                                      notes="improvement 7: rerank_page_strict + answer verifier"),
    # ---- round 2 (after retiring test-v1; chosen on dev only) ----
    "dense_b2": AgentConfig("dense_b2", method="dense", top_k=5, collection="colorme3_B2",
                            notes="baseline dense on index B2 (vision v3 gpt-4.1 captions)"),
    "hybrid_page_verify_b2": AgentConfig("hybrid_page_verify_b2", method="hybrid", top_k=5, allow_read_page=True,
                                         prompt="v2", verify=True, collection="colorme3_B2",
                                         notes="round-1 selection, index B2 (isolates the index change)"),
    "hpv2_b2": AgentConfig("hpv2_b2", method="hybrid", top_k=5, allow_read_page=True, prompt="v3", verify=True,
                           verify_version="v2", collection="colorme3_B2",
                           notes="round 2: + prompt v3 (numbers/abstain/masthead rules) + verifier v2"),
    "hpv2_b": AgentConfig("hpv2_b", method="hybrid", top_k=5, allow_read_page=True, prompt="v3", verify=True,
                          verify_version="v2", collection="colorme3_B",
                          notes="ablation: round-2 agent on old index B (isolates prompt/verifier change)"),
    "rpv2_b2": AgentConfig("rpv2_b2", method="rerank", top_k=5, allow_read_page=True, prompt="v3", verify=True,
                           verify_version="v2", collection="colorme3_B2",
                           notes="round 2 with LLM rerank"),
    "hpv2_b3": AgentConfig("hpv2_b3", method="hybrid", top_k=5, allow_read_page=True, prompt="v3", verify=True,
                           verify_version="v2", collection="colorme3_B3",
                           notes="round 2 on index B3 = text + vision v2 + vision v3 (union)"),
    "rpv2_b3": AgentConfig("rpv2_b3", method="rerank", top_k=5, allow_read_page=True, prompt="v3", verify=True,
                           verify_version="v2", collection="colorme3_B3", notes="round 2 + rerank on B3"),
    "hpv2_b3_k8": AgentConfig("hpv2_b3_k8", method="hybrid", top_k=8, allow_read_page=True, prompt="v3", verify=True,
                              verify_version="v2", collection="colorme3_B3",
                              notes="B3 has ~1.5x chunks per page -> top-8"),
    # ---- round 3: GPT-5.6 Luna (Responses API, reasoning) + filter fixes; chosen on dev only ----
    "luna_hpv2_b": AgentConfig("luna_hpv2_b", method="hybrid", top_k=5, allow_read_page=True, prompt="v3", verify=True,
                               verify_version="v2", model="gpt-5.6-luna", reasoning="low",
                               notes="round-2 selection with the model swapped to gpt-5.6-luna (isolates model)"),
    "luna_v4_fb": AgentConfig("luna_v4_fb", method="hybrid", top_k=5, allow_read_page=True, prompt="v4", verify=True,
                              verify_version="v3", model="gpt-5.6-luna", reasoning="low", filter_mode="fallback",
                              notes="luna + prompt v4 (filter rules) + filtered/unfiltered merge + verifier v3"),
    "luna_v4_none": AgentConfig("luna_v4_none", method="hybrid", top_k=5, allow_read_page=True, prompt="v4", verify=True,
                                verify_version="v3", model="gpt-5.6-luna", reasoning="low", filter_mode="none",
                                notes="luna + prompt v4 + no chapter filter at all + verifier v3"),
    "luna_v4_fb_b3": AgentConfig("luna_v4_fb_b3", method="hybrid", top_k=5, allow_read_page=True, prompt="v4",
                                 verify=True, verify_version="v3", model="gpt-5.6-luna", reasoning="low", filter_mode="fallback",
                                 collection="colorme3_B3", notes="luna_v4_fb on index B3 (vision v2 + v3)"),
    "luna_v4_fb_med": AgentConfig("luna_v4_fb_med", method="hybrid", top_k=5, allow_read_page=True, prompt="v4",
                                  verify=True, verify_version="v3", model="gpt-5.6-luna", reasoning="medium", filter_mode="fallback",
                                  notes="luna_v4_fb with reasoning effort medium"),
    "luna_v4_fb_b4": AgentConfig("luna_v4_fb_b4", method="hybrid", top_k=5, allow_read_page=True, prompt="v4",
                                 verify=True, verify_version="v3", model="gpt-5.6-luna", reasoning="low",
                                 filter_mode="fallback", collection="colorme3_B4",
                                 notes="luna_v4_fb on index B4 = text + gpt-5.6-luna vision descriptions"),
    "hpv2_b_v4fb": AgentConfig("hpv2_b_v4fb", method="hybrid", top_k=5, allow_read_page=True, prompt="v4", verify=True,
                               verify_version="v3", filter_mode="fallback",
                               notes="ablation: round-3 filter/verifier changes with gpt-4.1-mini (isolates model)"),
    "rerank_page_41": AgentConfig("rerank_page_41", method="rerank", top_k=5, allow_read_page=True,
                                  model="gpt-4.1", notes="defined but not run: rerank_page with gpt-4.1 controller"),
}
GROUPS = ["table", "image", "chart", "multihop", "text", "unanswerable"]


def log(msg: str) -> None:
    print(msg, flush=True)


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text)).strip().casefold()


def load_bench() -> list[dict[str, Any]]:
    return json.loads(config.BENCH_FILE.read_text(encoding="utf-8"))["questions"]


def bench_hash() -> str:
    data = json.loads(config.BENCH_FILE.read_text(encoding="utf-8"))
    core = [{k: q[k] for k in sorted(q)} for q in data["questions"]]
    return hashlib.sha256(json.dumps(core, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


# ------------------------------------------------------------------ evidence matching
def gold_groups(q: dict[str, Any]) -> list[list[dict[str, Any]]]:
    """Evidence groups: every group must be covered; items inside a group are alternatives."""
    groups: dict[str, list[dict[str, Any]]] = {}
    for g in q.get("gold", []):
        groups.setdefault(g.get("group", "g1"), []).append(g)
    return list(groups.values())


def chunk_supports(chunk: dict[str, Any], g: dict[str, Any]) -> bool:
    return (chunk["source_id"] == g["source_id"] and chunk["page"] == g["page"]
            and norm(g["evidence"]) in norm(chunk["text"]))


def coverage(q: dict[str, Any], chunks: list[dict[str, Any]]) -> dict[str, Any]:
    groups = gold_groups(q)
    covered = [any(chunk_supports(c, g) for c in chunks for g in grp) for grp in groups]
    return {"all": bool(groups) and all(covered), "any": any(covered), "groups": covered}


def first_hit_rank(q: dict[str, Any], ranked: list[dict[str, Any]]) -> int | None:
    for i, c in enumerate(ranked, 1):
        if any(chunk_supports(c, g) for grp in gold_groups(q) for g in grp):
            return i
    return None


# ------------------------------------------------------------------ commands
def cmd_export(args) -> None:
    store = Day6Store(args.collection)
    chunks = store.all_chunks()
    write_json(config.chunks_file(args.collection), chunks)
    kinds: dict[str, int] = {}
    for c in chunks:
        kinds[c["metadata"]["content_type"]] = kinds.get(c["metadata"]["content_type"], 0) + 1
    stats = {"day6_root": str(config.DAY6_ROOT), "collection": args.collection,
             "collection_metadata": store.collection_meta, "chunks": len(chunks), "by_content_type": kinds,
             "pages_covered": len({c["page"] for c in chunks}),
             "exported_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    write_json(config.RESULTS / f"export_stats_{args.collection}.json", stats)
    log(json.dumps(stats, ensure_ascii=False))


def cmd_validate(args) -> None:
    chunks = load_chunks(args.collection)
    qs = load_bench()
    problems = []
    ids = set()
    for q in qs:
        if q["id"] in ids:
            problems.append(f"duplicate id {q['id']}")
        ids.add(q["id"])
        if q["group"] not in GROUPS:
            problems.append(f"{q['id']}: bad group {q['group']}")
        if q["answerable"]:
            for grp in gold_groups(q):
                for g in grp:
                    if not any(chunk_supports(c, g) for c in chunks):
                        problems.append(f"{q['id']}: evidence not inside any chunk of p{g['page']}: {g['evidence'][:50]!r}")
        elif q.get("expected_behavior") != "search_and_abstain":
            problems.append(f"{q['id']}: unanswerable needs expected_behavior=search_and_abstain")
    counts = {s: {g: sum(1 for q in qs if q["split"] == s and q["group"] == g) for g in GROUPS} for s in ("dev", "test", "test_v1", "test_v2")}
    for p in problems:
        log("PROBLEM " + p)
    log(json.dumps(counts, ensure_ascii=False))
    log(f"benchmark sha256 {bench_hash()}")
    if problems:
        sys.exit(1)


def cmd_retrieval(args) -> None:
    """Single-query retrieval with the ORIGINAL question (no rewrite, no filter) for every method."""
    chunks = load_chunks(args.collection)
    qs = [q for q in load_bench() if q["split"] == args.split and q["answerable"]]
    rows, traces = [], []
    for method in args.methods.split(","):
        r = build(method, chunks, args.collection)
        u0 = USAGE.snapshot()
        t0 = time.perf_counter()
        per = []
        for q in qs:
            ranked = r.search(q["question"], top_k=10)
            rank = first_hit_rank(q, ranked)
            cov3 = coverage(q, ranked[:3])
            pages3 = {c["page"] for c in ranked[:3]}
            gold_pages = {g["page"] for grp in gold_groups(q) for g in grp}
            per.append({"id": q["id"], "group": q["group"], "hit1": rank == 1, "hit3": cov3["all"],
                        "hit3_any_group": cov3["any"], "page_hit3": bool(pages3 & gold_pages),
                        "rr10": 1 / rank if rank else 0.0})
            traces.append({"method": method, "query_id": q["id"], "split": q["split"], "group": q["group"],
                           "query": q["question"], "filter": None, "first_hit_rank": rank,
                           "results": [{"id": c["id"], "page": c["page"], "rank": c["rank"], "score": c["score"],
                                        "content_type": c["metadata"]["content_type"],
                                        "hit": any(chunk_supports(c, g) for grp in gold_groups(q) for g in grp)}
                                       for c in ranked]})
        elapsed = time.perf_counter() - t0
        u1 = USAGE.snapshot()
        cost = sum(v["cost_usd"] for v in u1.values()) - sum(v["cost_usd"] for v in u0.values())
        n = len(per)
        row = {"method": method, "split": args.split, "N": n,
               "hit1": sum(p["hit1"] for p in per), "hit3": sum(p["hit3"] for p in per),
               "hit3_any_group": sum(p["hit3_any_group"] for p in per),
               "page_hit3": sum(p["page_hit3"] for p in per),
               "mrr10": round(sum(p["rr10"] for p in per) / n, 3),
               "by_group_hit3": {g: f"{sum(p['hit3'] for p in per if p['group'] == g)}/"
                                    f"{sum(1 for p in per if p['group'] == g)}" for g in GROUPS[:-1]},
               "seconds": round(elapsed, 2), "ms_per_query": round(elapsed / n * 1000, 1),
               "cost_usd": round(cost, 5)}
        rows.append(row)
        log(f"{method:7s} {args.split}: Hit@1 {row['hit1']}/{n}  EvidenceHit@3 {row['hit3']}/{n} "
            f"(any-group {row['hit3_any_group']})  PageHit@3 {row['page_hit3']}/{n}  MRR@10 {row['mrr10']}  "
            f"{row['ms_per_query']} ms/q  ${row['cost_usd']}")
    out = config.RESULTS / "retrieval" / (args.split if args.collection == "colorme3_B" else f"{args.split}_{args.collection}")
    write_json(out / "summary.json", {"benchmark_sha256": bench_hash(), "query": "original question, no filter",
                                      "collection": args.collection,
                                      "run_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "rows": rows})
    write_json(out / "traces.json", traces)


def cmd_agent(args) -> None:
    cfg = CONFIGS[args.config]
    chunks = load_chunks(cfg.collection)
    retriever = build(cfg.method, chunks, cfg.collection)
    client = openai_client()
    agent = Agent(cfg, retriever, chunks, client)
    qs = [q for q in load_bench() if q["split"] == args.split]
    if args.ids:
        qs = [q for q in qs if q["id"] in set(args.ids.split(","))]
    u0 = USAGE.snapshot()
    t0 = time.perf_counter()
    # only id + question go to the agent; gold stays here
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        results = list(ex.map(lambda q: agent.run(q["question"], q["id"]), qs))
    wall = time.perf_counter() - t0
    by_id = {q["id"]: q for q in qs}
    for r in results:
        q = by_id[r["query_id"]]
        r["split"], r["group"], r["answerable"] = q["split"], q["group"], q["answerable"]
        shown = [c for c in chunks if c["id"] in set(r["context_ids"])]
        r["context_evidence"] = coverage(q, shown) if q["answerable"] else None
    u1 = USAGE.snapshot()
    usage = {k: {m: round(u1[k][m] - u0.get(k, {}).get(m, 0), 6) for m in u1[k]} for k in u1}
    ans = [r for r in results if r["answerable"]]
    ok = [r for r in results if r["status"] != "error"]
    calls = [r["n_retrieval_calls"] for r in ok]
    summary = {
        "config": cfg.name, "agent_config": results[0]["agent_config"] if results else None, "split": args.split,
        "benchmark_sha256": bench_hash(), "run_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "N": len(results), "status": {s: sum(r["status"] == s for r in results) for s in ("answered", "abstain", "error")},
        "context_evidence_rate": f"{sum(r['context_evidence']['all'] for r in ans)}/{len(ans)}",
        "context_evidence_by_group": {g: f"{sum(r['context_evidence']['all'] for r in ans if r['group'] == g)}/"
                                         f"{sum(1 for r in ans if r['group'] == g)}" for g in GROUPS[:-1]},
        "answered_on_answerable": f"{sum(r['status'] == 'answered' for r in ans)}/{len(ans)}",
        "abstained_on_unanswerable": f"{sum(r['status'] == 'abstain' for r in results if not r['answerable'])}/"
                                     f"{sum(1 for r in results if not r['answerable'])}",
        "tool_use": f"{sum(c > 0 for c in calls)}/{len(ok)}",
        "retrieval_calls": {"mean": round(statistics.mean(calls), 2) if calls else None,
                            "dist": {str(k): calls.count(k) for k in sorted(set(calls))}},
        "context_chars_mean": round(statistics.mean(r["context_chars"] for r in ok), 1) if ok else None,
        "latency_s": {"median": round(statistics.median(r["latency_s"] for r in results), 2),
                      "max": max(r["latency_s"] for r in results), "wall_total": round(wall, 1)},
        "usage": usage, "cost_usd_total": round(sum(v["cost_usd"] for v in usage.values()), 4),
        "errors": [{"id": r["query_id"], "error": r["error"]} for r in results if r["status"] == "error"],
    }
    out = config.RESULTS / "agent" / cfg.name / args.split
    write_json(out / "traces.json", sorted(results, key=lambda r: r["query_id"]))
    write_json(out / "summary.json", summary)
    log(json.dumps({k: summary[k] for k in ("config", "split", "status", "context_evidence_rate",
                                            "answered_on_answerable", "abstained_on_unanswerable", "tool_use",
                                            "retrieval_calls", "latency_s", "cost_usd_total")}, ensure_ascii=False))


def cmd_sheet(args) -> None:
    """Markdown sheet: question, expected answer, gold evidence, agent answer, cited chunks."""
    out = config.RESULTS / "agent" / args.config / args.split
    traces = json.loads((out / "traces.json").read_text(encoding="utf-8"))
    chunks = {c["id"]: c for c in load_chunks()}
    bench = {q["id"]: q for q in load_bench()}
    lines = [f"# Review sheet {args.config} / {args.split}\n"]
    for t in traces:
        q = bench[t["query_id"]]
        lines.append(f"\n## {q['id']} [{q['group']}] status={t['status']} retrieval_calls={t['n_retrieval_calls']}")
        lines.append(f"**Q:** {q['question']}")
        if q["answerable"]:
            lines.append(f"**Expected:** {q['expected_answer']}")
            lines.append("**Gold:** " + "; ".join(f"p{g['page']} ({g.get('evidence_type')}) `{g['evidence'][:80]}`"
                                                   for g in q["gold"]))
            lines.append(f"**Context evidence:** {t['context_evidence']}")
        else:
            lines.append(f"**Expected:** abstain — {q.get('absence_reason')}")
        lines.append(f"**Answer:** {t['answer']}")
        for cid in t["citations"]:
            c = chunks.get(cid)
            lines.append(f"- `{cid}` p{c['page'] if c else '?'}: " + (c["text"][:400].replace("\n", " ") if c else "MISSING"))
        lines.append("**Searches:** " + " | ".join(f"{e['tool']}({e['query']!r}, {e['filter']})"
                                                   for e in t["events"] if e["event"] == "search"))
    (out / "review_sheet.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    log(f"wrote {out / 'review_sheet.md'}")


def cmd_score(args) -> None:
    """Aggregate manual labels (results/labels/<config>_<split>.json) into pass rates per group
    and write the starter agent_metrics input files."""
    out = config.RESULTS / "agent" / args.config / args.split
    traces = {t["query_id"]: t for t in json.loads((out / "traces.json").read_text(encoding="utf-8"))}
    labels = json.loads((config.RESULTS / "labels" / f"{args.config}_{args.split}.json").read_text(encoding="utf-8"))
    bench = {q["id"]: q for q in load_bench() if q["split"] == args.split}
    lab = {l["query_id"]: l for l in labels}
    missing = set(bench) - set(lab)
    if missing:
        sys.exit(f"missing labels: {sorted(missing)}")
    rows = {}
    for g in GROUPS:
        ids = [i for i, q in bench.items() if q["group"] == g]
        rows[g] = {"pass": sum(lab[i]["pass"] for i in ids), "N": len(ids)}
    total = sum(r["pass"] for r in rows.values())
    N = len(bench)
    report = {"config": args.config, "split": args.split, "by_group": rows,
              "pass": total, "N": N, "pass_rate": round(total / N, 4),
              "system_errors": sum(t["status"] == "error" for t in traces.values()),
              "failed_ids": sorted(i for i in bench if not lab[i]["pass"])}
    write_json(out / "pass_summary.json", report)
    # agent_metrics.py inputs
    cases = [{"id": i, "split": q["split"], "answerable": q["answerable"]} for i, q in bench.items()]
    tr = [{"query_id": i, "status": traces[i]["status"], "events": traces[i]["events"],
           "citations": traces[i]["citations"]} for i in bench]
    rv = []
    for i, q in bench.items():
        l = lab[i]
        r = {"query_id": i, "citation_support": l["citation_support"]}
        if q["answerable"]:
            r["answer_grade"] = l["answer_grade"]
        else:
            r["abstention_correct"] = l["abstention_correct"]
        rv.append(r)
    for name, obj in (("cases.json", cases), ("agent_traces.json", tr), ("reviews.json", rv)):
        write_json(out / "metrics_input" / name, obj)
    log(json.dumps(report, ensure_ascii=False))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("export")
    p.add_argument("--collection", default="colorme3_B")
    p = sub.add_parser("validate")
    p.add_argument("--collection", default="colorme3_B")
    p = sub.add_parser("retrieval")
    p.add_argument("--split", required=True, choices=["dev", "test", "test_v1", "test_v2"])
    p.add_argument("--methods", default="dense,bm25,hybrid,rerank")
    p.add_argument("--collection", default="colorme3_B")
    p = sub.add_parser("agent")
    p.add_argument("--config", required=True, choices=list(CONFIGS))
    p.add_argument("--split", required=True, choices=["dev", "test", "test_v1", "test_v2"])
    p.add_argument("--ids", default="")
    p.add_argument("--workers", type=int, default=4)
    for name in ("sheet", "score"):
        p = sub.add_parser(name)
        p.add_argument("--config", required=True)
        p.add_argument("--split", required=True, choices=["dev", "test", "test_v1", "test_v2"])
    args = ap.parse_args()
    {"export": cmd_export, "validate": cmd_validate, "retrieval": cmd_retrieval, "agent": cmd_agent,
     "sheet": cmd_sheet, "score": cmd_score}[args.cmd](args)


if __name__ == "__main__":
    main()
