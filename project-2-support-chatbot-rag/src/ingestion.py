"""Knowledge base ingestion: load docs → chunk → embed → store in ChromaDB.

No external API calls — embeddings are produced by the deterministic
hashing vectorizer in `embeddings.py`, so ingestion runs fully offline.
"""

from __future__ import annotations

from pathlib import Path

import chromadb
from loguru import logger

from .config import Settings
from .embeddings import embed_batch
from .exceptions import IngestionError
from .models import DocumentChunk, IngestionResult


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    """Split text into overlapping word-count windows.

    Returns an empty list for blank input. `overlap` must be smaller than
    `chunk_size` or the sliding window never advances.
    """
    words = text.split()
    if not words:
        return []

    if overlap >= chunk_size:
        overlap = max(0, chunk_size - 1)

    chunks: list[str] = []
    start = 0
    step = chunk_size - overlap
    while start < len(words):
        window = words[start : start + chunk_size]
        chunks.append(" ".join(window))
        start += step

    return chunks


def load_knowledge_base(kb_dir: Path) -> list[tuple[str, str]]:
    """Load every `.md` file in `kb_dir` as (filename, text) pairs.

    Raises IngestionError if the directory does not exist or contains no
    markdown documents.
    """
    if not kb_dir.exists() or not kb_dir.is_dir():
        raise IngestionError(f"Knowledge base directory not found: {kb_dir}")

    docs: list[tuple[str, str]] = []
    for path in sorted(kb_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8").strip()
        if text:
            docs.append((path.name, text))
        else:
            logger.warning(f"Skipping empty knowledge base document: {path.name}")

    if not docs:
        raise IngestionError(f"No markdown documents found in {kb_dir}")

    logger.info(f"Loaded {len(docs)} knowledge base documents from {kb_dir}")
    return docs


def get_chroma_collection(settings: Settings) -> chromadb.Collection:
    """Get or create the persistent ChromaDB collection used for retrieval.

    We pass our own embeddings on every add/query call, so no embedding
    function is registered on the collection.
    """
    client = chromadb.PersistentClient(
        path=settings.chroma_persist_dir,
        settings=chromadb.Settings(anonymized_telemetry=False),
    )
    return client.get_or_create_collection(
        name=settings.collection_name,
        metadata={"hnsw:space": "cosine"},
    )


def ingest_documents(settings: Settings, kb_dir: Path | None = None) -> IngestionResult:
    """Chunk, embed, and store every document in the knowledge base.

    The collection is cleared and rebuilt on each run so re-ingestion is
    idempotent. Raises IngestionError on failure.
    """
    target_dir = kb_dir or Path(settings.knowledge_base_dir)
    logger.info(f"Starting knowledge base ingestion from {target_dir}")

    try:
        docs = load_knowledge_base(target_dir)
        collection = get_chroma_collection(settings)

        existing_ids = collection.get()["ids"]
        if existing_ids:
            collection.delete(ids=existing_ids)

        all_chunks: list[DocumentChunk] = []
        for filename, text in docs:
            pieces = chunk_text(text, settings.chunk_size, settings.chunk_overlap)
            for idx, piece in enumerate(pieces):
                all_chunks.append(
                    DocumentChunk(source=filename, text=piece, chunk_index=idx)
                )

        if not all_chunks:
            raise IngestionError("Chunking produced zero chunks from the knowledge base")

        embeddings = embed_batch([c.text for c in all_chunks], settings.embedding_dim)

        collection.add(
            ids=[c.id for c in all_chunks],
            embeddings=embeddings,
            documents=[c.text for c in all_chunks],
            metadatas=[{"source": c.source, "chunk_index": c.chunk_index} for c in all_chunks],
        )

        result = IngestionResult(
            total_documents=len(docs),
            total_chunks=len(all_chunks),
            collection_name=settings.collection_name,
        )
        logger.info(
            f"Ingestion complete — {result.total_documents} docs, "
            f"{result.total_chunks} chunks stored in '{result.collection_name}'"
        )
        return result

    except IngestionError:
        raise
    except Exception as exc:  # noqa: BLE001
        logger.error(f"Ingestion failed: {exc}")
        raise IngestionError(f"Ingestion failed: {exc}") from exc


if __name__ == "__main__":
    from .config import settings, setup_logging

    setup_logging(settings.log_level)
    ingest_documents(settings)
