class CryptoSystemError(Exception):
    """Base exception class for CryptoSystem."""
    pass


class ServiceNotFoundError(CryptoSystemError):
    """Raised when a requested service is not found in the registry."""
    pass


class ConfigurationError(CryptoSystemError):
    """Raised when configuration loading or parsing fails."""
    pass
