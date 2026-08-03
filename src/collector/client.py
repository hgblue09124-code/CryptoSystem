from abc import ABC, abstractmethod
from typing import List
from src.shared.models import Candle, Ticker
from src.shared.enums import Timeframe


class BaseExchangeClient(ABC):
    """Abstract Base Class for exchange clients."""

    @abstractmethod
    def fetch_ticker(self, symbol: str) -> Ticker:
        """Fetch current ticker price for a symbol."""
        pass

    @abstractmethod
    def fetch_ohlcv(
        self, symbol: str, timeframe: Timeframe, limit: int = 100
    ) -> List[Candle]:
        """Fetch historical OHLCV candles for a symbol."""
        pass
