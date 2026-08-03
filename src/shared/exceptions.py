from src.core.exceptions import CryptoSystemError


class SharedModelError(CryptoSystemError):
    """Base exception for shared model validation or processing errors."""
    pass


class ValidationError(SharedModelError):
    """Raised when data model validation fails."""
    pass
