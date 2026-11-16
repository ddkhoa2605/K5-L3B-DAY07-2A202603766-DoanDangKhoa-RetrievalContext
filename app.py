"""Streamlit UI để test Day 7 Agentic RAG (EBOOK COLORME 3).

Chạy từ thư mục repo:   streamlit run app.py
Cần: Day 6 Chroma (DAY6_ROOT), file export data/colorme_chunks*.json, OPENAI_API_KEY (.env hoặc Day 6 starter/.env).
"""
from __future__ import annotations

import json
import time
from dataclasses import asdict, replace
from pathlib import Path

import pandas as pd
import streamlit as st

from src import config
from src.agent import Agent
from src.cli import CONFIGS, GROUPS, chunk_supports, coverage, gold_groups
from src.retrievers import USAGE, build, load_chunks, openai_client

st.set_page_config(page_title="ColorME RAG", page_icon="🎨", layout="wide")

COLLECTIONS = [c for c in ("colorme3_B", "colorme3_B2", "colorme3_B3", "colorme3_B4") if config.chunks_file(c).exists()]
METHODS = ["dense", "bm25", "hybrid", "rerank"]
CHAPTERS = ["", "front", "ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8", "appendix"]
DEFAULT_CFG = "luna_v4_fb_b4" if "luna_v4_fb_b4" in CONFIGS else "hpv2_b"


# ------------------------------------------------------------------ cached resources
@st.cache_resource(show_spinner="Đang nạp chunks…")
def get_chunks(collection: str):
    return load_chunks(collection)


@st.cache_resource(show_spinner="Đang khởi tạo retriever…")
def get_retriever(method: str, collection: str):
    return build(method, get_chunks(collection), collection)


@st.cache_resource
def get_client():
    return openai_client()


@st.cache_data
def get_bench():
    return json.loads(config.BENCH_FILE.read_text(encoding="utf-8"))["questions"]


def page_image(page: int) -> Path | None:
    p = config.PAGE_IMAGES / f"p{page:03d}.png"
    return p if p.exists() else None


def show_chunk(c: dict, hit: bool | None = None, img: bool = True, key: str = "") -> None:
    m = c["metadata"]
    tag = "🟢 HIT · " if hit else ""
    title = (f"{tag}#{c.get('rank', '')} `{c['id']}` · trang PDF {c['page']} (in {m.get('printed_page')}) · "
             f"{m.get('content_type')} · {m.get('chapter')} · score {c.get('score', '')}")
    with st.expander(title):
        cols = st.columns([3, 2]) if img else [st.container()]
        cols[0].text(c["text"])
        if img and (pi := page_image(c["page"])):
            cols[1].image(str(pi), caption=f"Trang PDF {c['page']}", use_container_width=True)


def run_agent(cfg_name: str, question: str, overrides: dict, qid: str = "ui") -> dict:
    cfg = replace(CONFIGS[cfg_name], **overrides)
    chunks = get_chunks(cfg.collection)
    agent = Agent(cfg, get_retriever(cfg.method, cfg.collection), chunks, get_client())
    before = USAGE.snapshot()
    t0 = time.perf_counter()
    res = agent.run(question, qid)
    after = USAGE.snapshot()
    res["ui_total_cost"] = round(sum(v["cost_usd"] for v in after.values()) - sum(v["cost_usd"] for v in before.values()), 5)
    res["ui_wall_s"] = round(time.perf_counter() - t0, 2)
    return res


def show_result(res: dict, q: dict | None = None) -> None:
    status = res["status"]
    icon = {"answered": "✅", "abstain": "🚫", "error": "❌"}.get(status, "")
    st.markdown(f"**{icon} {status.upper()}**")
    if res.get("error"):
        st.error(res["error"])
    st.markdown(res["answer"] or "_(trống)_")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Thời gian", f"{res['ui_wall_s']} s")
    c2.metric("Lượt retrieval", res["n_retrieval_calls"])
    c3.metric("Token in/out", f"{res['tokens_in']}/{res['tokens_out']}")
    c4.metric("Chi phí (agent+verify+embed)", f"${res['ui_total_cost']}")
    if q is not None:
        if q.get("answerable"):
            shown = [c for c in get_chunks(res["agent_config"]["collection"]) if c["id"] in set(res["context_ids"])]
            cov = coverage(q, shown)
            st.info(f"**Đáp án chuẩn:** {q['expected_answer']}  \n"
                    f"Context có đủ evidence gold: **{'có' if cov['all'] else 'không'}** (theo group: {cov['groups']})")
        else:
            st.info(f"**Mong đợi:** từ chối — {q.get('absence_reason')}  \n"
                    f"Agent: **{'đã từ chối' if status == 'abstain' else 'KHÔNG từ chối'}**")
    by_id = {c["id"]: c for c in get_chunks(res["agent_config"]["collection"])}
    if res["citations"]:
        st.markdown("**Citation**")
        for cid in res["citations"]:
            if cid in by_id:
                show_chunk(by_id[cid], key=cid)
    with st.expander("🔧 Trace tool call"):
        rows = []
        for e in res["events"]:
            if e["event"] == "search":
                rows.append({"tool": e["tool"], "query": e["query"], "filter": json.dumps(e.get("filter"), ensure_ascii=False),
                             "kết quả": ", ".join(f"p{r['page']}:{r['content_type'][0]}" for r in e["results"]),
                             "thêm vào context": len(e["added_ids"]), "bỏ (budget)": len(e["dropped_ids"]),
                             "lỗi": e.get("error") or "", "s": e.get("latency_s")})
        if rows:
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        for e in res["events"]:
            if e["event"] == "verify":
                st.markdown("**Verifier** – bản nháp trước khi kiểm chứng:")
                st.text(e["draft_answer"])
                if e.get("removed_claims"):
                    st.markdown("Ý bị xóa: " + " · ".join(e["removed_claims"]))
            elif e["event"] not in ("search", "model"):
                st.caption(f"event: {json.dumps(e, ensure_ascii=False)[:300]}")
        st.json({"model_calls": res["n_model_calls"], "context_pages": res["context_pages"],
                 "context_chars": res["context_chars"], "config": res["agent_config"]}, expanded=False)
    with st.expander(f"📚 Context cuối gửi model ({len(res['context_ids'])} chunk)"):
        st.text(res["context"] or "(trống)")


def config_picker(key: str, default: str = DEFAULT_CFG) -> tuple[str, dict]:
    names = list(CONFIGS)
    name = st.selectbox("Cấu hình agent", names, index=names.index(default), key=f"{key}_cfg")
    cfg = CONFIGS[name]
    st.caption(f"{cfg.model} · {cfg.method} · {cfg.collection} · prompt {cfg.prompt} · "
               f"filter {cfg.filter_mode} · verify {cfg.verify_version if cfg.verify else '—'} — {cfg.notes}")
    ov = {}
    with st.expander("Ghi đè tham số (tuỳ chọn)"):
        a, b, c = st.columns(3)
        top_k = a.number_input("top_k", 1, 15, cfg.top_k, key=f"{key}_k")
        steps = b.number_input("max_steps", 1, 10, cfg.max_steps, key=f"{key}_s")
        budget = c.number_input("budget (ký tự)", 1000, 40000, cfg.budget, step=1000, key=f"{key}_b")
        d, e, f = st.columns(3)
        coll = d.selectbox("collection", COLLECTIONS, index=COLLECTIONS.index(cfg.collection)
                           if cfg.collection in COLLECTIONS else 0, key=f"{key}_c")
        fm = e.selectbox("filter_mode", ["agent", "fallback", "none"], index=["agent", "fallback", "none"].index(cfg.filter_mode),
                         key=f"{key}_f")
        ver = f.checkbox("verifier", cfg.verify, key=f"{key}_v")
        if config.is_reasoning(cfg.model):
            ov["reasoning"] = st.selectbox("reasoning effort", ["none", "low", "medium", "high"],
                                           index=["none", "low", "medium", "high"].index(cfg.reasoning), key=f"{key}_r")
    ov.update(top_k=int(top_k), max_steps=int(steps), budget=int(budget), collection=coll, filter_mode=fm, verify=ver)
    return name, {k: v for k, v in ov.items() if getattr(cfg, k) != v}


# ------------------------------------------------------------------ layout
st.title("🎨 ColorME Agentic RAG — bàn test")
st.caption(f"Day 6 index: `{config.CHROMA_DIR}` · collections có sẵn: {', '.join(COLLECTIONS)}")

tab_ask, tab_ret, tab_bench, tab_res, tab_page = st.tabs(
    ["💬 Hỏi agent", "🔎 Retrieval", "📋 Benchmark", "📊 Kết quả đã lưu", "📄 Trang sách"])

# ---- 1. Ask
with tab_ask:
    compare = st.toggle("So sánh 2 cấu hình", value=False)
    cols = st.columns(2) if compare else [st.container()]
    picks = []
    for i, col in enumerate(cols):
        with col:
            picks.append(config_picker(f"ask{i}", DEFAULT_CFG if i == 0 else "dense"))
    bench = get_bench()
    ex = st.selectbox("Hoặc chọn câu mẫu từ benchmark", ["(tự nhập)"] + [f"{q['id']} [{q['split']}/{q['group']}] {q['question']}" for q in bench])
    q_obj = None if ex == "(tự nhập)" else next(q for q in bench if q["id"] == ex.split(" ")[0])
    question = st.text_area("Câu hỏi", value=q_obj["question"] if q_obj else "", height=80,
                            placeholder="vd: Màu bổ túc của tím là gì và thương hiệu nào được lấy làm ví dụ?")
    if st.button("Hỏi", type="primary", disabled=not question.strip()):
        for col, (name, ov) in zip(cols, picks):
            with col:
                st.subheader(name + (f" (ghi đè: {ov})" if ov else ""))
                with st.spinner("Agent đang tìm và trả lời…"):
                    try:
                        res = run_agent(name, question.strip(), ov, q_obj["id"] if q_obj else "ui")
                    except Exception as exc:  # show provider/store errors instead of crashing
                        st.error(f"{type(exc).__name__}: {exc}")
                        continue
                show_result(res, q_obj)

# ---- 2. Retrieval
with tab_ret:
    a, b, c, d = st.columns([3, 1, 1, 1])
    rq = a.text_input("Truy vấn", placeholder="vd: thanh màu tím trong bảng màu logo")
    method = b.selectbox("Phương pháp", METHODS, index=2)
    coll = c.selectbox("Collection", COLLECTIONS, index=COLLECTIONS.index("colorme3_B4") if "colorme3_B4" in COLLECTIONS else 0)
    k = d.number_input("top_k", 1, 20, 5)
    e, f, g = st.columns(3)
    chap = e.selectbox("Lọc chương", CHAPTERS)
    ctype = f.selectbox("Lọc loại", ["", "text", "visual"])
    gq = g.selectbox("Đánh dấu hit theo câu benchmark", ["(không)"] + [q["id"] for q in get_bench() if q["answerable"]])
    if st.button("Tìm", type="primary", disabled=not rq.strip()):
        filters = {kk: v for kk, v in (("chapter", chap), ("content_type", ctype)) if v} or None
        t0 = time.perf_counter()
        try:
            res = get_retriever(method, coll).search(rq, filters=filters, top_k=int(k))
        except Exception as exc:
            st.error(f"{type(exc).__name__}: {exc}")
            res = []
        st.caption(f"{len(res)} kết quả · {round((time.perf_counter() - t0) * 1000)} ms · filter {filters}")
        gold_q = next((q for q in get_bench() if q["id"] == gq), None)
        if gold_q:
            st.caption("Gold: " + "; ".join(f"p{g['page']} `{g['evidence'][:60]}`" for grp in gold_groups(gold_q) for g in grp))
        st.dataframe(pd.DataFrame([{"rank": r["rank"], "id": r["id"], "page": r["page"], "loại": r["metadata"]["content_type"],
                                    "chương": r["metadata"]["chapter"], "score": r["score"],
                                    "hit": any(chunk_supports(r, g) for grp in gold_groups(gold_q) for g in grp) if gold_q else None}
                                   for r in res]), use_container_width=True, hide_index=True)
        for r in res:
            show_chunk(r, any(chunk_supports(r, g) for grp in gold_groups(gold_q) for g in grp) if gold_q else None)

# ---- 3. Benchmark
with tab_bench:
    bench = get_bench()
    a, b = st.columns(2)
    split = a.selectbox("Split", ["dev", "test", "test_v1", "test_v2"])
    groups = b.multiselect("Nhóm", GROUPS, default=GROUPS)
    sub = [q for q in bench if q["split"] == split and q["group"] in groups]
    st.dataframe(pd.DataFrame([{"id": q["id"], "nhóm": q["group"], "câu hỏi": q["question"],
                                "đáp án / hành vi": q.get("expected_answer") or "TỪ CHỐI",
                                "trang gold": ", ".join(str(g["page"]) for g in q.get("gold", []))} for q in sub]),
                 use_container_width=True, hide_index=True, height=280)
    if sub:
        qid = st.selectbox("Xem / chạy một câu", [q["id"] for q in sub])
        q = next(x for x in sub if x["id"] == qid)
        st.markdown(f"**{q['question']}**")
        if q["answerable"]:
            st.markdown(f"Đáp án chuẩn: {q['expected_answer']}")
            pages = sorted({g["page"] for g in q["gold"]})
            for g in q["gold"]:
                st.caption(f"p{g['page']} · {g.get('evidence_type')} · group {g.get('group', 'g1')} · `{g['evidence']}` "
                           f"{'· vùng: ' + g['region'] if g.get('region') else ''}")
            imgs = [page_image(p) for p in pages[:4] if page_image(p)]
            if imgs:
                st.image([str(i) for i in imgs], width=260, caption=[f"PDF p{p}" for p in pages[:len(imgs)]])
        else:
            st.markdown(f"Mong đợi: **từ chối** — {q['absence_reason']}  \nCách kiểm tra: {q['check_method']}")
        name, ov = config_picker("bench")
        if st.button("Chạy câu này"):
            with st.spinner("Đang chạy…"):
                show_result(run_agent(name, q["question"], ov, q["id"]), q)
        st.divider()
        st.markdown(f"**Chạy cả {len(sub)} câu đang lọc** với cấu hình trên (tốn API; kết quả chỉ hiển thị, không ghi đè `results/`).")
        if st.button(f"Chạy {len(sub)} câu"):
            prog = st.progress(0.0)
            rows = []
            for i, qq in enumerate(sub):
                try:
                    r = run_agent(name, qq["question"], ov, qq["id"])
                    shown = [c for c in get_chunks(r["agent_config"]["collection"]) if c["id"] in set(r["context_ids"])]
                    ctx = coverage(qq, shown)["all"] if qq["answerable"] else None
                    rows.append({"id": qq["id"], "nhóm": qq["group"], "status": r["status"],
                                 "đúng hành vi?": (r["status"] == "answered") if qq["answerable"] else (r["status"] == "abstain"),
                                 "context đủ evidence": ctx, "trả lời": r["answer"][:200],
                                 "chuẩn": qq.get("expected_answer") or "TỪ CHỐI", "s": r["ui_wall_s"], "$": r["ui_total_cost"]})
                except Exception as exc:
                    rows.append({"id": qq["id"], "status": "error", "trả lời": str(exc)[:200]})
                prog.progress((i + 1) / len(sub))
            df = pd.DataFrame(rows)
            st.dataframe(df, use_container_width=True, hide_index=True)
            if "đúng hành vi?" in df:
                st.success(f"Đúng hành vi (trả lời/từ chối): {int(df['đúng hành vi?'].fillna(False).sum())}/{len(df)} · "
                           f"tổng chi phí ${round(df['$'].fillna(0).sum(), 4)}. Đúng/sai nội dung vẫn cần chấm tay.")

# ---- 4. Saved results
with tab_res:
    adir = config.RESULTS / "agent"
    runs = sorted(f"{p.parent.name}/{p.name}" for p in adir.glob("*/*") if (p / "summary.json").exists())
    sel = st.selectbox("Lần chạy đã lưu (config/split)", runs,
                       index=runs.index(f"{DEFAULT_CFG}/test") if f"{DEFAULT_CFG}/test" in runs else 0)
    if sel:
        d = adir / sel
        s = json.loads((d / "summary.json").read_text(encoding="utf-8"))
        a, b, c, e = st.columns(4)
        a.metric("Context evidence", s["context_evidence_rate"])
        b.metric("Từ chối đúng (câu thiếu evidence)", s["abstained_on_unanswerable"])
        c.metric("Median latency", f"{s['latency_s']['median']} s")
        e.metric("Chi phí", f"${s['cost_usd_total']}")
        cfg_name, split = sel.split("/")
        lab_file = config.RESULTS / "labels" / f"{cfg_name}_{split}.json"
        labels = {l["query_id"]: l for l in json.loads(lab_file.read_text(encoding="utf-8"))} if lab_file.exists() else {}
        if labels:
            n = sum(l["pass"] for l in labels.values())
            st.success(f"Chấm tay: **{n}/{len(labels)} đạt ({n / len(labels):.1%})**")
            by = pd.DataFrame(labels.values()).groupby("group")["pass"].agg(["sum", "count"])
            st.dataframe(by.rename(columns={"sum": "đạt", "count": "tổng"}).T, use_container_width=True)
        traces = json.loads((d / "traces.json").read_text(encoding="utf-8"))
        only_fail = st.checkbox("Chỉ hiện câu không đạt", value=False, disabled=not labels)
        for t in traces:
            l = labels.get(t["query_id"])
            if only_fail and l and l["pass"]:
                continue
            mark = "" if not l else ("✅" if l["pass"] else "❌")
            with st.expander(f"{mark} {t['query_id']} [{t.get('group')}] {t['status']} — {t['question'][:90]}"):
                st.markdown(t["answer"])
                if l:
                    st.caption(f"Nhãn: {l['reason']}")
                st.caption(f"citations: {t['citations']} · retrieval calls {t['n_retrieval_calls']} · {t['latency_s']} s")
                st.dataframe(pd.DataFrame([{"tool": e["tool"], "query": e["query"], "filter": json.dumps(e.get("filter"), ensure_ascii=False),
                                            "kết quả": ", ".join(f"p{r['page']}" for r in e["results"])}
                                           for e in t["events"] if e["event"] == "search"]), hide_index=True, use_container_width=True)
        with st.expander("summary.json"):
            st.json(s, expanded=False)

# ---- 5. Page viewer
with tab_page:
    a, b = st.columns([1, 3])
    page = a.number_input("Trang PDF (1-183)", 1, 183, 136)
    coll = a.selectbox("Mô tả hình từ collection", COLLECTIONS, index=COLLECTIONS.index("colorme3_B4") if "colorme3_B4" in COLLECTIONS else 0,
                       key="page_coll")
    if (pi := page_image(int(page))):
        a.image(str(pi), caption=f"PDF p{page} (in {page - 1})", use_container_width=True)
    with b:
        for c in sorted((c for c in get_chunks(coll) if c["page"] == page), key=lambda c: c["id"]):
            st.markdown(f"**`{c['id']}`** · {c['metadata']['content_type']} · {c['metadata'].get('visual_kind', '')}")
            st.text(c["text"])
