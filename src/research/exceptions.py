from src.core.exceptions import CryptoSystemError


class ResearchError(CryptoSystemError):
    """Base exception for all research and indicator calculation errors."""
    pass


class InsufficientDataError(ResearchError):
    """Raised when there are not enough candles to calculate an indicator."""
    pass
