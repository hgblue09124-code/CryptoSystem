from typing import List
from src.shared.models import Candle
from src.research.exceptions import InsufficientDataError


class TechnicalIndicators:
    """Provides pure mathematical implementations of technical indicators."""

    @staticmethod
    def calculate_sma(candles: List[Candle], period: int) -> float:
        if len(candles) < period:
            raise InsufficientDataError(
                f"Need at least {period} candles for SMA, got {len(candles)}"
            )
        close_prices = [c.close for c in candles[-period:]]
        return sum(close_prices) / period

    @staticmethod
    def calculate_ema(candles: List[Candle], period: int) -> float:
        if len(candles) < period:
            raise InsufficientDataError(
                f"Need at least {period} candles for EMA, got {len(candles)}"
            )
        multiplier = 2 / (period + 1)
        ema = sum([c.close for c in candles[:period]]) / period
        for candle in candles[period:]:
            ema = (candle.close - ema) * multiplier + ema
        return ema

    @staticmethod
    def calculate_rsi(candles: List[Candle], period: int = 14) -> float:
        if len(candles) < period + 1:
            raise InsufficientDataError(
                f"Need at least {period + 1} candles for RSI, got {len(candles)}"
            )
        
        gains = []
        losses = []
        for i in range(1, len(candles)):
            change = candles[i].close - candles[i - 1].close
            if change >= 0:
                gains.append(change)
                losses.append(0.0)
            else:
                gains.append(0.0)
                losses.append(abs(change))

        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period

        if avg_loss == 0:
            return 100.0

        rs = avg_gain / avg_loss
        return 100.0 - (100.0 / (1.0 + rs))
