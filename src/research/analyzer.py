from typing import List, Dict, Any
from src.core.logger import get_logger
from src.shared.models import Candle
from src.research.indicators import TechnicalIndicators

logger = get_logger("MarketAnalyzer")


class MarketAnalyzer:
    """Analyzes candle data and returns technical analysis metrics."""

    def analyze_market(self, candles: List[Candle]) -> Dict[str, Any]:
        logger.info(f"Analyzing market metrics for {len(candles)} candles...")
        
        sma_20 = TechnicalIndicators.calculate_sma(candles, period=20)
        ema_50 = TechnicalIndicators.calculate_ema(candles, period=50)
        rsi_14 = TechnicalIndicators.calculate_rsi(candles, period=14)

        return {
            "latest_close": candles[-1].close,
            "sma_20": round(sma_20, 2),
            "ema_50": round(ema_50, 2),
            "rsi_14": round(rsi_14, 2),
            "trend": "BULLISH" if candles[-1].close > sma_20 else "BEARISH",
        }
