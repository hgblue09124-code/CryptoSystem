from src.core.exceptions import CryptoSystemError


class RiskError(CryptoSystemError):
    """Base exception for all risk validation errors."""
    pass


class RiskCheckFailedError(RiskError):
    """Raised when a signal violates risk parameters."""
    pass
