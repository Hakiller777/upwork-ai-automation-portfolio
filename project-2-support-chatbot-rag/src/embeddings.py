"""Deterministic, offline text embeddings (hashing-trick vectorizer).

No network calls and no model download — keeps the demo fully self-hosted
and dependency-light. In production, swap `embed_text` for a real embedding
model (e.g. an embeddings API or a local sentence-transformers model); every
other module only depends on the `embed_text` / `embed_batch` signatures.
"""

from __future__ import annotations

import hashlib
import math
import re

_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


def _token_index(token: str, dim: int) -> int:
    """Deterministic hash → vector index (stable across processes/runs)."""
    digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
    return int(digest, 16) % dim


def embed_text(text: str, dim: int = 256) -> list[float]:
    """Embed a single string as an L2-normalized term-frequency hash vector.

    Empty or whitespace-only text returns a zero vector.
    """
    vector = [0.0] * dim
    tokens = _tokenize(text)

    if not tokens:
        return vector

    for token in tokens:
        vector[_token_index(token, dim)] += 1.0

    norm = math.sqrt(sum(v * v for v in vector))
    if norm > 0:
        vector = [v / norm for v in vector]
    return vector


def embed_batch(texts: list[str], dim: int = 256) -> list[list[float]]:
    """Embed a batch of strings. Order-preserving."""
    return [embed_text(text, dim) for text in texts]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Cosine similarity between two vectors of equal length.

    Returns 0.0 for zero-magnitude vectors instead of raising.
    """
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return max(0.0, min(1.0, dot / (norm_a * norm_b)))
