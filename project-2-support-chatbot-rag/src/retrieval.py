"""Vector search: embed a query, fetch top-k chunks, rank by similarity."""

from __future__ import annotations

import chromadb
from loguru import logger

from .config import Settings
from .embeddings import embed_text
from .exceptions import RetrievalError
from .ingestion import get_chroma_collection
from .models import RetrievedChunk


def _distance_to_similarity(distance: float) -> float:
    """Convert ChromaDB cosine distance (0=identical, 2=opposite) to a
    0-1 similarity score."""
    similarity = 1.0 - (distance / 2.0)
    return max(0.0, min(1.0, similarity))


def retrieve(
    query: str,
    settings: Settings,
    collection: chromadb.Collection | None = None,
) -> list[RetrievedChunk]:
    """Return the top-k most relevant chunks for a support query.

    Returns an empty list for blank queries or an empty/unseeded collection
    rather than raising — callers (agent.py) treat that as "no context found".
    Raises RetrievalError if the vector store query itself fails.
    """
    if not query or not query.strip():
        logger.warning("Retrieval called with empty query — returning no results")
        return []

    try:
        coll = collection or get_chroma_collection(settings)

        if coll.count() == 0:
            logger.warning("Knowledge base collection is empty — run ingestion first")
            return []

        query_embedding = embed_text(query, settings.embedding_dim)
        n_results = min(settings.top_k, coll.count())

        raw = coll.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=["documents", "metadatas", "distances"],
        )

        chunks: list[RetrievedChunk] = []
        ids = raw["ids"][0]
        documents = raw["documents"][0]
        metadatas = raw["metadatas"][0]
        distances = raw["distances"][0]

        for chunk_id, text, metadata, distance in zip(ids, documents, metadatas, distances):
            chunks.append(
                RetrievedChunk(
                    chunk_id=chunk_id,
                    source=metadata.get("source", "unknown"),
                    text=text,
                    score=_distance_to_similarity(distance),
                )
            )

        chunks.sort(key=lambda c: c.score, reverse=True)
        logger.info(f"Retrieved {len(chunks)} chunks for query: '{query[:60]}'")
        return chunks

    except RetrievalError:
        raise
    except Exception as exc:  # noqa: BLE001
        logger.error(f"Retrieval failed for query '{query[:60]}': {exc}")
        raise RetrievalError(f"Retrieval failed: {exc}") from exc
