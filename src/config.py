"""Paths, models and prices shared by the Day 7 code.

Day 6 artefacts are read in place (no copy of the vector store):
- Chroma persistent store  <DAY6_ROOT>/starter/chroma_db, collection ``colorme3_B``
  (text chunks + vision-description chunks, OpenAI text-embedding-3-small, 1536-d, cosine)
- page metadata / renders  <DAY6_ROOT>/data/pages.jsonl, data/page_images/
Override the location with the DAY6_ROOT environment variable.
"""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAY6_ROOT = Path(os.environ.get("DAY6_ROOT", ROOT.parents[1] / "day6" / "K5-L3-Day06-ColorME"))
CHROMA_DIR = DAY6_ROOT / "starter" / "chroma_db"
DAY6_COLLECTION = os.environ.get("DAY6_COLLECTION", "colorme3_B")
DAY6_PAGES = DAY6_ROOT / "data" / "pages.jsonl"
PAGE_IMAGES = DAY6_ROOT / "data" / "page_images"

DATA = ROOT / "data"
CHUNKS_FILE = DATA / "colorme_chunks.json"      # export of colorme3_B (for BM25 / audit)


def chunks_file(collection: str) -> Path:
    """Export file per Day 6 collection (colorme3_B -> colorme_chunks.json, others suffixed)."""
    return CHUNKS_FILE if collection == "colorme3_B" else DATA / f"colorme_chunks_{collection}.json"
BENCH_FILE = ROOT / "benchmark" / "questions.json"
RESULTS = ROOT / "results"

EMBED_MODEL = "text-embedding-3-small"
EMBED_DIM = 1536
AGENT_MODEL = os.environ.get("AGENT_MODEL", "gpt-4.1-mini")
RERANK_MODEL = os.environ.get("RERANK_MODEL", "gpt-4.1-mini")

# USD per 1M tokens: (input, output)
PRICES = {"gpt-4.1-mini": (0.40, 1.60), "gpt-4.1": (2.00, 8.00), "gpt-4.1-nano": (0.10, 0.40),
          "gpt-4o-mini": (0.15, 0.60), "text-embedding-3-small": (0.02, 0.0),
          # gpt-5.6-luna: $0.20 / $1.20 per 1M (list price after the 2026-07-30 cut, from secondary
          # sources; official rate card not verified) – reasoning tokens are billed as output.
          "gpt-5.6-luna": (0.20, 1.20)}


def is_reasoning(model: str) -> bool:
    """gpt-5.x / o-series: no temperature; tools + reasoning need the Responses API."""
    return model.startswith(("gpt-5", "gpt-6", "o1", "o3", "o4"))


def cost(model: str, tokens_in: int, tokens_out: int = 0) -> float:
    base = next((k for k in sorted(PRICES, key=len, reverse=True) if model.startswith(k)), None)
    pin, pout = PRICES.get(base, (0.0, 0.0))
    return tokens_in / 1e6 * pin + tokens_out / 1e6 * pout


def load_env() -> None:
    """Load OPENAI_API_KEY from ./.env, falling back to the Day 6 starter/.env."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    for p in (ROOT / ".env", DAY6_ROOT / "starter" / ".env"):
        if p.exists():
            load_dotenv(p)
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY not found in .env or Day 6 starter/.env")
