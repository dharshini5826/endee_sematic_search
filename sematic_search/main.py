"""
main.py — Semantic Search Demo
================================
Demonstrates the full semantic search pipeline:
  1. Build index from documents
  2. Run example queries
  3. Interactive search loop
  4. Pairwise similarity demo

Run:
    python main.py
    python main.py --query "heart problems"
    python main.py --query "AI learning" --top_k 3 --threshold 0.4
"""

import argparse
import time

from search_engine import SemanticSearchEngine
from data import DOCUMENTS
from utils import print_results, print_similarity_matrix


# ─────────────────────────────────────────
#  Example queries to demonstrate semantic
#  (not keyword) matching
# ─────────────────────────────────────────
DEMO_QUERIES = [
    # Query                  → should surface
    "problems with the heart",              # Medical docs (no exact keyword match)
    "how machines learn from data",         # ML / Deep Learning
    "saving the environment from pollution",# Climate / Renewable
    "making money by investing",            # Finance docs
    "relaxation and reducing anxiety",      # Mental health / Yoga
]


def run_demo(engine: SemanticSearchEngine):
    """Run all pre-defined demo queries and print results."""
    print("\n" + "=" * 64)
    print("  DEMO MODE — Running example queries")
    print("=" * 64)

    for query in DEMO_QUERIES:
        t0 = time.time()
        results = engine.search(query, top_k=3, threshold=0.3)
        elapsed = time.time() - t0
        print_results(results, query, len(DOCUMENTS), elapsed)
        input("  Press Enter for next query...")


def run_similarity_demo(engine: SemanticSearchEngine):
    """Show pairwise similarity between a few texts."""
    sample_texts = [
        "cardiac arrest and chest pain",
        "heart disease treatment",
        "stock market investment",
        "cryptocurrency trading",
        "deep learning model training",
    ]
    print_similarity_matrix(engine, sample_texts)


def interactive_loop(engine: SemanticSearchEngine, top_k: int, threshold: float):
    """Let the user type queries interactively."""
    print("\n" + "=" * 64)
    print("  INTERACTIVE MODE  (type 'quit' to exit, 'demo' for examples)")
    print("=" * 64 + "\n")

    while True:
        try:
            query = input("  🔍  Enter query: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n  Goodbye!")
            break

        if not query:
            continue
        if query.lower() in ("quit", "exit", "q"):
            print("  Goodbye!")
            break
        if query.lower() == "demo":
            run_demo(engine)
            continue
        if query.lower() == "sim":
            run_similarity_demo(engine)
            continue

        t0 = time.time()
        results = engine.search(query, top_k=top_k, threshold=threshold)
        elapsed = time.time() - t0
        print_results(results, query, len(DOCUMENTS), elapsed)


# ─────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Semantic Search with TensorFlow Universal Sentence Encoder"
    )
    parser.add_argument("--query",     type=str,   default=None,  help="Single query to run")
    parser.add_argument("--top_k",     type=int,   default=5,     help="Max results to return")
    parser.add_argument("--threshold", type=float, default=0.2,   help="Min similarity score")
    parser.add_argument("--demo",      action="store_true",       help="Run demo queries")
    parser.add_argument("--sim",       action="store_true",       help="Show similarity matrix")
    args = parser.parse_args()

    # ── 1. Load model & build index ──────────────────────────────────────────
    engine = SemanticSearchEngine()
    engine.build_index(DOCUMENTS)

    # Optionally save the index so it loads faster next time:
    # engine.save_index("index")
    # engine.load_index("index")   ← skips re-encoding on next run

    # ── 2. Choose mode ───────────────────────────────────────────────────────
    if args.query:
        t0 = time.time()
        results = engine.search(args.query, top_k=args.top_k, threshold=args.threshold)
        elapsed = time.time() - t0
        print_results(results, args.query, len(DOCUMENTS), elapsed)

    elif args.demo:
        run_demo(engine)

    elif args.sim:
        run_similarity_demo(engine)

    else:
        # Default: interactive
        interactive_loop(engine, top_k=args.top_k, threshold=args.threshold)


if __name__ == "__main__":
    main()