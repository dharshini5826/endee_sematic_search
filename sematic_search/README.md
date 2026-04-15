# Semantic Search with TensorFlow

A Python semantic search engine using **TensorFlow** and Google's
**Universal Sentence Encoder (USE)** to find documents by *meaning*,
not just keywords.

---

## How Semantic Search Works

```
Your Query ──► [USE Encoder] ──► Query Vector (512-dim)
                                        │
                                  Cosine Similarity
                                        │
Documents ───► [USE Encoder] ──► Doc Vectors (N × 512)
                                        │
                                  Ranked Results ◄──
```

1. **Embedding** — Both query and documents are converted into 512-dimensional
   vectors by the Universal Sentence Encoder
2. **Cosine Similarity** — Measures the angle between two vectors
   (1.0 = identical meaning, 0.0 = unrelated)
3. **Ranking** — Documents are sorted by similarity score

---

## Project Structure

```
semantic_search_tf/
│
├── search_engine.py   ← Core engine: encode, index, search
├── data.py            ← 20 sample documents (5 categories)
├── utils.py           ← Pretty terminal output helpers
├── main.py            ← Entry point: demo, interactive, CLI
└── requirements.txt   ← Dependencies
```

---

## Setup

```bash
# 1. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python main.py
```

> The Universal Sentence Encoder (~1 GB) is auto-downloaded from
> TensorFlow Hub on first run and cached locally.

---

## Usage

### Interactive mode (default)
```bash
python main.py
```
Type any natural language query and get ranked results.
Special commands inside interactive mode:
- `demo`  → runs 5 pre-defined example queries
- `sim`   → prints a pairwise similarity matrix
- `quit`  → exits

### Single query via CLI
```bash
python main.py --query "heart problems"
python main.py --query "AI learning" --top_k 3
python main.py --query "saving the environment" --threshold 0.5
```

### Flags
| Flag          | Default | Description                    |
|---------------|---------|--------------------------------|
| `--query`     | None    | Run a single query and exit    |
| `--top_k`     | 5       | Number of results to return    |
| `--threshold` | 0.2     | Minimum similarity score       |
| `--demo`      | False   | Run built-in demo queries      |
| `--sim`       | False   | Show pairwise similarity demo  |

---

## Example Output

```
  Semantic Search
  Query   : heart problems
  Corpus  : 20 documents
  ────────────────────────────────────────────────────────────

  #1  Heart Disease Overview  [Medical]
      ████████████████░░░░  0.8912  ● Strong
      Heart disease refers to conditions affecting the heart...

  #2  Cardiac Health Tips  [Medical]
      █████████████░░░░░░░  0.7634  ● Strong
      Maintaining cardiac health involves regular exercise...

  #3  Nutrition and Diet  [Medical]
      ██████████░░░░░░░░░░  0.5201  ● Partial
      A healthy diet includes fruits, vegetables...

  Found 3 result(s) in 0.043s
```

---

## Key Concept: Semantic vs Keyword Search

| Query               | Keyword Search         | Semantic Search         |
|---------------------|------------------------|-------------------------|
| "heart problems"    | Needs exact word match | Finds "cardiac disease" |
| "AI learning"       | Misses synonyms        | Finds "machine learning"|
| "planet pollution"  | Rigid matching         | Finds "climate change"  |

---

## Saving & Reusing the Index

Encoding is slow on first run (~5s). Save the index to skip re-encoding:

```python
engine.build_index(DOCUMENTS)
engine.save_index("index")      # saves embeddings.npy + documents.json

# Later runs:
engine.load_index("index")      # instant — no re-encoding needed
```

---

## Adding Your Own Documents

Edit `data.py` and add entries to the `DOCUMENTS` list:

```python
{
    "id"      : 21,
    "title"   : "Your Document Title",
    "content" : "The full text content of your document goes here.",
    "category": "YourCategory"
}
```

Then rebuild the index:
```python
engine.build_index(DOCUMENTS)
```