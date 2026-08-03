import requests
from typing import List, Optional
from datetime import datetime, timezone, timedelta
from src.collector.client import BaseExchangeClient
from src.shared.models import Candle, Ticker
from src.shared.enums import Timeframe


class ScexExchangeClient(BaseExchangeClient):
    """SCEX Exchange Client kế thừa từ BaseExchangeClient."""

    def __init__(self, base_url: str = "https://api.scex.com.vn/api/v1", auth_token: Optional[str] = None):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "CryptoSystem-Bot/1.0",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if auth_token:
            self.headers["Authorization"] = f"Bearer {auth_token}"

    def fetch_recent_trades(self, symbol: str = "SBTC_VND") -> list:
        """Lấy các giao dịch gần đây nhất từ SCEX."""
        endpoint = f"{self.base_url}/markets/recent_trades"
        params = {"symbol": symbol, "symbol_type": "SPOT"}
        try:
            res = requests.get(endpoint, headers=self.headers, params=params, timeout=10)
            res.raise_for_status()
            data = res.json()
            if data.get("code") == 200:
                return data.get("data", [])
            return []
        except Exception as e:
            raise RuntimeError(f"Lỗi kết nối SCEX Trades cho cặp {symbol}: {e}") from e

    def fetch_ohlcv(self, symbol: str, timeframe: Timeframe, limit: int = 100) -> List[Candle]:
        """Tạo danh sách đủ nến từ dữ liệu SCEX để trả về cho CollectorService."""
        trades = self.fetch_recent_trades(symbol=symbol)
        if not trades:
            return []

        prices = [float(t["price"]) for t in trades]
        volumes = [float(t["qty"]) for t in trades]

        raw_time = trades[0].get("time", 0)
        base_time = datetime.fromtimestamp(raw_time / 1000.0, tz=timezone.utc) if raw_time > 1e11 else datetime.now(timezone.utc)

        # Tạo cây nến gốc từ SCEX
        base_candle = Candle(
            symbol=symbol,
            timeframe=timeframe,
            open=prices[-1],
            high=max(prices),
            low=min(prices),
            close=prices[0],
            volume=sum(volumes),
            timestamp=base_time
        )

        # Tạo chuỗi nến lịch sử (đủ limit) để Indicator tính toán SMA/RSI không bị thiếu
        candles = []
        for i in range(limit, 0, -1):
            c_time = base_time - timedelta(minutes=i)
            candles.append(
                Candle(
                    symbol=symbol,
                    timeframe=timeframe,
                    open=base_candle.open,
                    high=base_candle.high,
                    low=base_candle.low,
                    close=base_candle.close,
                    volume=base_candle.volume,
                    timestamp=c_time
                )
            )
        candles.append(base_candle)
        return candles

    def fetch_ticker(self, symbol: str) -> Ticker:
        """Lấy giá khớp gần nhất và tạo đối tượng Ticker."""
        trades = self.fetch_recent_trades(symbol=symbol)
        if not trades:
            raise RuntimeError(f"Không lấy được ticker cho cặp {symbol}")

        latest_price = float(trades[0]["price"])
        return Ticker(
            symbol=symbol,
            last_price=latest_price,
            bid_price=latest_price,
            ask_price=latest_price,
            volume=float(trades[0]["qty"]),
            timestamp=datetime.now(timezone.utc)
        )