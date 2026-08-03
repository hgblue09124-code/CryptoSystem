from src.core.exceptions import CryptoSystemError


class DatabaseError(CryptoSystemError):
    """Base exception for all database errors."""
    pass


class DatabaseConnectionError(DatabaseError):
    """Raised when connecting to the database fails."""
    pass


class QueryExecutionError(DatabaseError):
    """Raised when a database query fails to execute."""
    pass
