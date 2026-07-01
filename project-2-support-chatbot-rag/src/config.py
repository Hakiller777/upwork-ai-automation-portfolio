"""Application settings and structured logging setup."""

import sys
from pathlib import Path

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All configuration read from environment variables / .env file."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # AI model used for answer generation (simulated in tests)
    claude_model: str = "claude-opus-4-8"

    # n8n webhook endpoint (simulated for demo)
    n8n_webhook_url: str = "http://n8n:5678/webhook/support-query"

    # Application behaviour
    log_level: str = "INFO"

    # Vector store (ChromaDB, embedded/self-hosted)
    chroma_persist_dir: str = "data/chroma_store"
    collection_name: str = "acmecrm_knowledge_base"
    knowledge_base_dir: str = "data/knowledge_base"

    # Embedding vectorizer (deterministic hashing trick — no external API)
    embedding_dim: int = 256

    # Chunking
    chunk_size: int = 120       # words per chunk
    chunk_overlap: int = 20     # words of overlap between consecutive chunks

    # Retrieval
    top_k: int = 4
    min_confidence_threshold: float = 0.15  # below this, agent returns a fallback answer


def setup_logging(log_level: str = "INFO") -> None:
    """Configure loguru for stdout + rotating file output."""
    logger.remove()
    logger.add(
        sys.stdout,
        level=log_level,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
        colorize=True,
    )
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    logger.add(
        log_dir / "rag.log",
        level=log_level,
        rotation="10 MB",
        retention="7 days",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{line} - {message}",
    )


settings = Settings()
