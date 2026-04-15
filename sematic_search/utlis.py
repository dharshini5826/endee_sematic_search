"""
Utility functions for displaying search results and similarity scores
in a clean, readable terminal format.
"""

# ANSI colour codes
RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
GREY   = "\033[90m"
RED    = "\033[91m"
WHITE  = "\033[97m"
BG_DARK = "\033[100m"

CATEGORY_COLORS = {
    "Medical"    : "\033[95m",   # magenta
    "Technology" : "\033[94m",   # blue
    "Environment": "\033[92m",   # green
    "Science"    : "\033[96m",   # cyan
    "Finance"    : "\033[93m",   # yellow
}


def score_bar(score: float, width: int = 20) -> str:
    """Return a coloured ASCII progress bar for a score (0.0–1.0)."""
    filled = int(score * width)
    bar    = "█" * filled + "░" * (width - filled)
    if score >= 0.75:
        color = GREEN
    elif score >= 0.50:
        color = YELLOW
    else:
        color = GREY
    return f"{color}{bar}{RESET}"


def score_label(score: float) -> str:
    if score >= 0.75:
        return f"{GREEN}●  Strong{RESET}"
    elif score >= 0.50:
        return f"{YELLOW}●  Partial{RESET}"
    elif score >= 0.30:
        return f"{GREY}●  Weak{RESET}"
    else:
        return f"{RED}●  Low{RESET}"


def print_header(query: str, total_docs: int):
    print()
    print(f"{BG_DARK}{BOLD}  Semantic Search  {RESET}")
    print(f"{CYAN}  Query   : {WHITE}{query}{RESET}")
    print(f"{CYAN}  Corpus  : {WHITE}{total_docs} documents{RESET}")
    print(f"  {'─' * 60}")


def print_results(results: list[dict], query: str, total_docs: int, elapsed: float):
    print_header(query, total_docs)

    if not results:
        print(f"\n  {GREY}No results found above the similarity threshold.{RESET}\n")
        return

    for r in results:
        cat_color = CATEGORY_COLORS.get(r["category"], WHITE)
        print()
        print(f"  {BOLD}#{r['rank']}{RESET}  {WHITE}{r['title']}{RESET}  "
              f"{cat_color}[{r['category']}]{RESET}")
        print(f"      {score_bar(r['score'])}  {r['score']:.4f}  {score_label(r['score'])}")
        # Wrap content at 70 chars
        words   = r["content"].split()
        line    = "      "
        lines   = []
        for w in words:
            if len(line) + len(w) + 1 > 74:
                lines.append(line)
                line = "      "
            line += w + " "
        lines.append(line)
        print(f"{GREY}{''.join(chr(10) + l for l in lines)}{RESET}")

    print()
    print(f"  {GREY}Found {len(results)} result(s) in {elapsed:.3f}s{RESET}")
    print(f"  {'─' * 60}")
    print()


def print_similarity_matrix(engine, texts: list[str]):
    """Print a similarity matrix for a list of texts — useful for debugging."""
    print(f"\n{BOLD}Pairwise Similarity Matrix{RESET}")
    n = len(texts)
    labels = [t[:20] + "…" if len(t) > 20 else t for t in texts]
    col_w = 8

    # Header row
    header = "  " + " " * 22
    for lb in labels:
        header += f"{lb[:col_w]:>{col_w}}  "
    print(header)

    for i, ta in enumerate(texts):
        row = f"  {labels[i]:<22}"
        for j, tb in enumerate(texts):
            sim = engine.similarity(ta, tb)
            if i == j:
                row += f"{GREY}{sim:>{col_w}.3f}{RESET}  "
            elif sim >= 0.7:
                row += f"{GREEN}{sim:>{col_w}.3f}{RESET}  "
            elif sim >= 0.4:
                row += f"{YELLOW}{sim:>{col_w}.3f}{RESET}  "
            else:
                row += f"{sim:>{col_w}.3f}  "
        print(row)
    print()