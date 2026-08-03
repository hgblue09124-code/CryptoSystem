from src.core.exceptions import CryptoSystemError


class DecisionError(CryptoSystemError):
    """Base exception for strategy and decision engine errors."""
    pass
