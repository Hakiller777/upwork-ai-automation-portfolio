"""AI-powered lead scoring using Claude.

Scores each enriched lead 1-10 based on company fit, pain point severity,
contact seniority, and product-market alignment.
Implemented Day 2.
"""

from loguru import logger

from .config import settings
from .models import Lead, LeadStatus, ScoringResult


_QUALIFICATION_TIERS: dict[str, range] = {
    "hot": range(settings.hot_threshold, 11),
    "warm": range(settings.warm_threshold, settings.hot_threshold),
    "cold": range(1, settings.warm_threshold),
}


def get_qualification_tier(score: int) -> str:
    """Map a numeric score (1-10) to a qualification tier label."""
    for tier, score_range in _QUALIFICATION_TIERS.items():
        if score in score_range:
            return tier
    return "cold"


def score_lead(lead: Lead) -> ScoringResult:
    """Score a single enriched lead using Claude AI.

    Analyzes industry fit, company size, pain point urgency, contact title
    authority, and alignment with the product interest to produce a
    1-10 score with detailed reasoning.
    """
    raise NotImplementedError("Implemented Day 2")


def score_batch(leads: list[Lead]) -> tuple[list[Lead], list[ScoringResult]]:
    """Score a batch of enriched leads.

    Returns updated leads (with score + status applied) and the raw
    ScoringResult list. Leads below min_score_threshold are marked
    DISQUALIFIED. Failures are logged and skipped.
    """
    raise NotImplementedError("Implemented Day 2")
