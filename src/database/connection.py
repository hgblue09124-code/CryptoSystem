import sqlite3
from pathlib import Path
from typing import Optional
from src.core.logger import get_logger
from src.database.exceptions import DatabaseConnectionError

logger = get_logger("DatabaseConnection")


class DatabaseConnection:
    """Manages SQLite database connections and transactions."""

    def __init__(self, db_path: str = "data/cryptosystem.db") -> None:
        self.db_path = Path(db_path)
        self._connection: Optional[sqlite3.Connection] = None

    def connect(self) -> sqlite3.Connection:
        if self._connection is None:
            try:
                self.db_path.parent.mkdir(parents=True, exist_ok=True)
                self._connection = sqlite3.connect(
                    self.db_path, check_same_thread=False
                )
                self._connection.row_factory = sqlite3.Row
                logger.info(f"Database connected successfully at {self.db_path}")
            except Exception as e:
                logger.error(f"Failed to connect to database: {e}")
                raise DatabaseConnectionError(f"Database connection failed: {e}") from e
        return self._connection

    def close(self) -> None:
        if self._connection:
            self._connection.close()
            self._connection = None
            logger.info("Database connection closed.")
