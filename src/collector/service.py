from typing import List
from src.core.logger import get_logger
from src.shared.models import Candle, Ticker
from src.shared.enums import Timeframe
from src.database.repository import CandleRepository
from src.collector.client import BaseExchangeClient

logger = get_logger("MarketCollectorService")


class ExchangeFetchError(Exception):
    """Custom exception khi thu thập dữ liệu từ sàn thất bại."""
    pass


class MarketCollectorService:
    """Service layer responsible for orchestrating market data collection and database persistence."""

    def __init__(
        self, client: BaseExchangeClient, candle_repo: CandleRepository
    ) -> None:
        self.client = client
        self.candle_repo = candle_repo

    def collect_and_store_candles(
        self, symbol: str, timeframe: Timeframe, limit: int = 100
    ) -> List[Candle]:
        """Collects candles from exchange and stores them into the database."""
        try:
            logger.info(f"Collecting candles for {symbol} - {timeframe.value}...")
            candles = self.client.fetch_ohlcv(symbol, timeframe, limit)
            
            for candle in candles:
                self.candle_repo.save_candle(candle)
                
            logger.info(f"Successfully stored {len(candles)} candles for {symbol}.")
            return candles
        except Exception as e:
            logger.error(f"Failed to collect and store candles for {symbol}: {e}")
            raise ExchangeFetchError(f"Collection failed for {symbol}: {e}") from e

    def get_latest_ticker(self, symbol: str) -> Ticker:
        """Fetches the latest ticker for a given symbol."""
        try:
            return self.client.fetch_ticker(symbol)
        except Exception as e:
            logger.error(f"Failed to fetch ticker for {symbol}: {e}")
            raise ExchangeFetchError(f"Ticker fetch failed for {symbol}: {e}") from e