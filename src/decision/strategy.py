from datetime import datetime, timezone
from typing import Dict, Any
from src.core.logger import get_logger
from src.shared.models import Signal
from src.shared.enums import SignalType
from src.decision.exceptions import DecisionError

logger = get_logger("RsiStrategy")


class RsiStrategy:
    """Generates trading signals based on RSI and Trend analysis."""

    def __init__(self, overbought: float = 70.0, oversold: float = 30.0) -> None:
        self.overbought = overbought
        self.oversold = oversold

    def evaluate(self, symbol: str, metrics: Dict[str, Any]) -> Signal:
        rsi = metrics.get("rsi_14")
        latest_price = metrics.get("latest_close")

        if rsi is None or latest_price is None:
            raise DecisionError("Missing required metrics for signal evaluation")

        signal_type = SignalType.NO_SIGNAL
        strength = 0.0

        if rsi <= self.oversold:
            signal_type = SignalType.ENTER_LONG
            strength = min(1.0, (self.oversold - rsi + 10) / 20)
            logger.info(f"Oversold detected for {symbol} (RSI: {rsi}). Generating ENTER_LONG signal.")
        elif rsi >= self.overbought:
            signal_type = SignalType.ENTER_SHORT
            strength = min(1.0, (rsi - self.overbought + 10) / 20)
            logger.info(f"Overbought detected for {symbol} (RSI: {rsi}). Generating ENTER_SHORT signal.")

        return Signal(
            symbol=symbol,
            signal_type=signal_type,
            strength=round(strength, 2),
            timestamp=datetime.now(timezone.utc),
            source_strategy="RsiStrategy",
            suggested_price=latest_price,
        )
