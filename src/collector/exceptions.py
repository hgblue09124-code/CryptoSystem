from src.core.exceptions import CryptoSystemError


class CollectorError(CryptoSystemError):
    """Base exception for all market collector errors."""
    pass


class ExchangeFetchError(CollectorError):
    """Raised when fetching data from the exchange fails."""
    pass


class InvalidSymbolError(CollectorError):
    """Raised when an invalid or unsupported symbol is requested."""
    pass
