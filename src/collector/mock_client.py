import random
from datetime import datetime, timezone
from typing import List
from src.core.logger import get_logger
from src.shared.models import Candle, Ticker
from src.shared.enums import Timeframe
from src.collector.client import BaseExchangeClient

logger = get_logger("MockExchangeClient")


class MockExchangeClient(BaseExchangeClient):
    """Mock Exchange Client for local development and testing without API keys."""

    def fetch_ticker(self, symbol: str) -> Ticker:
        base_price = 50000.0 if "BTC" in symbol else 3000.0
        bid = base_price - random.uniform(0.5, 5.0)
        ask = base_price + random.uniform(0.5, 5.0)
        
        logger.info(f"Fetched mock ticker for {symbol}")
        return Ticker(
            symbol=symbol,
            bid=round(bid, 2),
            ask=round(ask, 2),
            last=round((bid + ask) / 2, 2),
            volume_24h=round(random.uniform(1000.0, 5000.0), 2),
            timestamp=datetime.now(timezone.utc),
        )

    def fetch_ohlcv(
        self, symbol: str, timeframe: Timeframe, limit: int = 100
    ) -> List[Candle]:
        candles = []
        current_price = 50000.0 if "BTC" in symbol else 3000.0
        now = datetime.now(timezone.utc)

        for i in range(limit):
            open_p = current_price + random.uniform(-10.0, 10.0)
            high_p = open_p + random.uniform(1.0, 15.0)
            low_p = open_p - random.uniform(1.0, 15.0)
            close_p = random.uniform(low_p, high_p)
            volume = random.uniform(10.0, 100.0)

            candles.append(
                Candle(
                    symbol=symbol,
                    timeframe=timeframe,
                    timestamp=now,
                    open=round(open_p, 2),
                    high=round(high_p, 2),
                    low=round(low_p, 2),
                    close=round(close_p, 2),
                    volume=round(volume, 2),
                )
            )
            current_price = close_p

        logger.info(f"Fetched {len(candles)} mock candles for {symbol} ({timeframe.value})")
        return candles
