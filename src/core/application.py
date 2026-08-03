import logging
from src.core.lifecycle import LifecycleManager
from src.core.registry import ServiceRegistry


class Application:
    """Main Application Controller."""

    def __init__(self, logger: logging.Logger, registry: ServiceRegistry) -> None:
        self.logger = logger
        self.registry = registry
        self.lifecycle = LifecycleManager()

    def run(self) -> None:
        self.lifecycle.start()
        self.logger.info("CryptoSystem Application RUNNING")

    def shutdown(self) -> None:
        self.lifecycle.stop()
        self.logger.info("CryptoSystem Application STOPPED")
