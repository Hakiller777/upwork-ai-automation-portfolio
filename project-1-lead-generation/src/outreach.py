"""Personalized outreach message generation using Claude.

Generates subject lines and email body copy tailored to each lead's
pain points, industry context, and contact seniority.
Implemented Day 2.
"""

from loguru import logger

from .config import settings
from .models import Lead, LeadStatus, OutreachResult, ScoringResult


def generate_outreach(lead: Lead, scoring: ScoringResult) -> OutreachResult:
    """Generate a personalized outreach email for a single scored lead.

    Uses the lead's enriched company context, pain points, and score
    reasoning to craft a compelling subject line and message body.
    Only called for leads above the min_score_threshold.
    """
    raise NotImplementedError("Implemented Day 2")


def generate_outreach_batch(
    leads: list[Lead],
    scores: list[ScoringResult],
) -> tuple[list[Lead], list[OutreachResult]]:
    """Generate outreach for a batch of scored leads.

    Skips leads below min_score_threshold (already DISQUALIFIED).
    Returns updated leads (status = OUTREACHED) and OutreachResult list.
    Failures are logged and the lead is left in SCORED status.
    """
    raise NotImplementedError("Implemented Day 2")
