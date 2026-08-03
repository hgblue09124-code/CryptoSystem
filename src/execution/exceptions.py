from src.core.exceptions import CryptoSystemError


class ExecutionError(CryptoSystemError):
    """Base exception for execution engine errors."""
    pass


class OrderExecutionFailedError(ExecutionError):
    """Raised when executing an order on exchange fails."""
    pass
