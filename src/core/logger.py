import logging
import sys


def setup_logger(level: int = logging.INFO) -> None:
    """Configures the root logging settings."""
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
        force=True,
    )


def get_logger(name: str = "CryptoSystem") -> logging.Logger:
    """Returns a logger instance with the given name."""
    return logging.getLogger(name)
