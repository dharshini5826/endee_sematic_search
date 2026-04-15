"""
Semantic Search Engine using TensorFlow + Universal Sentence Encoder
======================================================================
Uses Google's Universal Sentence Encoder (USE) to convert text into
high-dimensional embeddings, then finds the most semantically similar
documents using cosine similarity.

How it works:
  1. Load the USE model from TensorFlow Hub
  2. Encode all documents into embedding vectors
  3. For a query, encode it the same way
  4. Compute cosine similarity between query and all documents
  5. Rank and return top-k results
"""

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import json
import os
import time


# ─────────────────────────────────────────
#  Model URL (Universal Sentence Encoder)
# ─────────────────────────────────────────
USE_MODEL_URL = "https://tfhub.dev/google/universal-sentence-encoder/4"


class SemanticSearchEngine:
    """
    Core semantic search engine.

    Attributes:
        model       : Loaded TF Hub USE model
        documents   : List of document dicts {id, title, content, category}
        embeddings  : np.ndarray of shape (N, 512) — one vector per document
    """

    def __init__(self, model_url: str = USE_MODEL_URL):
        print("Loading Universal Sentence Encoder...")
        print(f"  Model: {model_url}\n")
        self.model = hub.load(model_url)
        self.documents = []
        self.embeddings = None
        print("Model loaded successfully!\n")

    # ──────────────────────────────────────
    #  Encoding
    # ──────────────────────────────────────

    def _encode(self, texts: list[str]) -> np.ndarray:
        """
        Encode a list of strings into embedding vectors using USE.
        Returns an (N, 512) float32 numpy array.
        """
        tensors = self.model(texts)          # TF tensor of shape (N, 512)
        return tensors.numpy()               # Convert to numpy

    # ──────────────────────────────────────
    #  Index Building
    # ──────────────────────────────────────

    def build_index(self, documents: list[dict]):
        """
        Encode all documents and store their embeddings.

        Args:
            documents: list of dicts with keys: id, title, content, category
        """
        self.documents = documents
        texts = [f"{doc['title']}. {doc['content']}" for doc in documents]

        print(f"Building index for {len(texts)} documents...")
        t0 = time.time()
        self.embeddings = self._encode(texts)         # shape: (N, 512)
        self.embeddings = self._normalize(self.embeddings)  # unit vectors
        elapsed = time.time() - t0
        print(f"Index built in {elapsed:.2f}s  |  Shape: {self.embeddings.shape}\n")

    def save_index(self, path: str = "index"):
        """Save embeddings + documents to disk for reuse."""
        os.makedirs(path, exist_ok=True)
        np.save(f"{path}/embeddings.npy", self.embeddings)
        with open(f"{path}/documents.json", "w") as f:
            json.dump(self.documents, f, indent=2)
        print(f"Index saved to '{path}/'")

    def load_index(self, path: str = "index"):
        """Load a previously saved index from disk."""
        self.embeddings = np.load(f"{path}/embeddings.npy")
        with open(f"{path}/documents.json") as f:
            self.documents = json.load(f)
        print(f"Index loaded: {len(self.documents)} docs, dim={self.embeddings.shape[1]}")

    # ──────────────────────────────────────
    #  Search
    # ──────────────────────────────────────

    def search(self, query: str, top_k: int = 5, threshold: float = 0.0) -> list[dict]:
        """
        Find the top-k most semantically similar documents.

        Args:
            query     : Natural language search string
            top_k     : Maximum number of results to return
            threshold : Minimum cosine similarity score (0.0 to 1.0)

        Returns:
            List of dicts: {rank, score, title, content, category}
        """
        if self.embeddings is None:
            raise RuntimeError("Index not built. Call build_index() first.")

        # Encode and normalize the query
        query_vec = self._encode([query])              # shape: (1, 512)
        query_vec = self._normalize(query_vec)         # unit vector

        # Cosine similarity = dot product of two unit vectors
        # Shape: (N,)
        scores = np.dot(self.embeddings, query_vec.T).flatten()

        # Get sorted indices (highest score first)
        ranked_idx = np.argsort(scores)[::-1]

        results = []
        for rank, idx in enumerate(ranked_idx[:top_k], start=1):
            score = float(scores[idx])
            if score < threshold:
                break
            doc = self.documents[idx]
            results.append({
                "rank"    : rank,
                "score"   : round(score, 4),
                "id"      : doc["id"],
                "title"   : doc["title"],
                "content" : doc["content"],
                "category": doc["category"],
            })

        return results

    # ──────────────────────────────────────
    #  Helpers
    # ──────────────────────────────────────

    @staticmethod
    def _normalize(vectors: np.ndarray) -> np.ndarray:
        """L2-normalize each row so cosine similarity = dot product."""
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        norms = np.where(norms == 0, 1e-10, norms)   # avoid division by zero
        return vectors / norms

    def similarity(self, text_a: str, text_b: str) -> float:
        """
        Compute raw cosine similarity between two arbitrary strings.
        Useful for testing or comparing any two pieces of text.
        """
        vecs = self._encode([text_a, text_b])
        vecs = self._normalize(vecs)
        return float(np.dot(vecs[0], vecs[1]))