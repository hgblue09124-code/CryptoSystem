from dataclasses import dataclass
from typing import Dict, Any
from src.core.logger import get_logger

logger = get_logger("AIAdvisor")


@dataclass(slots=True, frozen=True)
class AIRecommendation:
    confidence_score: float
    summary: str
    suggested_risk_multiplier: float


class AIAdvisor:
    """Provides market recommendations. AI NEVER executes or places orders directly."""

    def analyze_regime(self, metrics: Dict[str, Any]) -> AIRecommendation:
        rsi = metrics.get("rsi_14", 50.0)
        trend = metrics.get("trend", "NEUTRAL")

        logger.info("AI Layer evaluating market regime and strategy confidence...")

        if trend == "BULLISH" and rsi < 40:
            return AIRecommendation(
                confidence_score=0.85,
                summary="High probability dip buy opportunity in bullish trend.",
                suggested_risk_multiplier=1.2,
            )
        elif trend == "BEARISH" and rsi > 60:
            return AIRecommendation(
                confidence_score=0.80,
                summary="High probability short entry in bearish trend.",
                suggested_risk_multiplier=1.0,
            )

        return AIRecommendation(
            confidence_score=0.50,
            summary="Market range-bound or neutral. Maintain normal risk limits.",
            suggested_risk_multiplier=1.0,
        )
