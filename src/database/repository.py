import sqlite3
from datetime import datetime
from typing import List, Optional
from src.core.logger import get_logger
from src.shared.models import Candle, Order, Position
from src.shared.enums import Timeframe, OrderSide, OrderType, OrderStatus, PositionSide
from src.database.exceptions import QueryExecutionError

logger = get_logger("DatabaseRepository")


class CandleRepository:
    """Handles database persistence for Candle models."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.conn = connection

    def save_candle(self, candle: Candle) -> None:
        sql = """
        INSERT OR REPLACE INTO candles (symbol, timeframe, timestamp, open, high, low, close, volume)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        try:
            with self.conn:
                self.conn.execute(sql, (
                    candle.symbol,
                    candle.timeframe.value,
                    candle.timestamp.isoformat(),
                    candle.open,
                    candle.high,
                    candle.low,
                    candle.close,
                    candle.volume,
                ))
        except sqlite3.Error as e:
            logger.error(f"Error saving candle for {candle.symbol}: {e}")
            raise QueryExecutionError(f"Save candle failed: {e}") from e

    def get_candles(self, symbol: str, timeframe: Timeframe, limit: int = 100) -> List[Candle]:
        sql = """
        SELECT symbol, timeframe, timestamp, open, high, low, close, volume
        FROM candles
        WHERE symbol = ? AND timeframe = ?
        ORDER BY timestamp DESC
        LIMIT ?;
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (symbol, timeframe.value, limit))
            rows = cursor.fetchall()
            candles = []
            for row in reversed(rows):
                candles.append(
                    Candle(
                        symbol=row["symbol"],
                        timeframe=Timeframe(row["timeframe"]),
                        timestamp=datetime.fromisoformat(row["timestamp"]),
                        open=row["open"],
                        high=row["high"],
                        low=row["low"],
                        close=row["close"],
                        volume=row["volume"],
                    )
                )
            return candles
        except sqlite3.Error as e:
            logger.error(f"Error fetching candles for {symbol}: {e}")
            raise QueryExecutionError(f"Get candles failed: {e}") from e


class OrderRepository:
    """Handles database persistence for Order models."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.conn = connection

    def save_order(self, order: Order) -> None:
        sql = """
        INSERT OR REPLACE INTO orders (order_id, symbol, side, order_type, price, quantity, filled_quantity, average_price, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        try:
            with self.conn:
                self.conn.execute(sql, (
                    order.order_id,
                    order.symbol,
                    order.side.value,
                    order.order_type.value,
                    order.price,
                    order.quantity,
                    order.filled_quantity,
                    order.average_price,
                    order.status.name,
                    order.created_at.isoformat(),
                ))
        except sqlite3.Error as e:
            logger.error(f"Error saving order {order.order_id}: {e}")
            raise QueryExecutionError(f"Save order failed: {e}") from e
