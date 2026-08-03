import sqlite3
from src.core.logger import get_logger
from src.database.exceptions import QueryExecutionError

logger = get_logger("DatabaseSchema")

CREATE_CANDLES_TABLE = """
CREATE TABLE IF NOT EXISTS candles (
    symbol TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    open REAL NOT NULL,
    high REAL NOT NULL,
    low REAL NOT NULL,
    close REAL NOT NULL,
    volume REAL NOT NULL,
    PRIMARY KEY (symbol, timeframe, timestamp)
);
"""

CREATE_ORDERS_TABLE = """
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    symbol TEXT NOT NULL,
    side TEXT NOT NULL,
    order_type TEXT NOT NULL,
    price REAL NOT NULL,
    quantity REAL NOT NULL,
    filled_quantity REAL NOT NULL,
    average_price REAL NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
);
"""

CREATE_POSITIONS_TABLE = """
CREATE TABLE IF NOT EXISTS positions (
    symbol TEXT PRIMARY KEY,
    side TEXT NOT NULL,
    entry_price REAL NOT NULL,
    quantity REAL NOT NULL,
    leverage INTEGER NOT NULL,
    unrealized_pnl REAL NOT NULL,
    liquidation_price REAL
);
"""


class SchemaManager:
    """Initializes and updates database schemas."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.conn = connection

    def initialize_schema(self) -> None:
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(CREATE_CANDLES_TABLE)
                cursor.execute(CREATE_ORDERS_TABLE)
                cursor.execute(CREATE_POSITIONS_TABLE)
            logger.info("Database schema initialized successfully.")
        except sqlite3.Error as e:
            logger.error(f"Failed to initialize database schema: {e}")
            raise QueryExecutionError(f"Schema initialization failed: {e}") from e
