from src.core.logger import setup_logger, get_logger
from src.core.registry import ServiceRegistry
from src.core.application import Application


class Bootstrap:
    """Bootstraps core services and constructs the Application instance."""

    def build(self) -> Application:
        setup_logger()
        logger = get_logger("Bootstrap")
        logger.info("Initializing Core Foundation...")

        registry = ServiceRegistry()
        registry.register("logger", logger)

        app = Application(logger=logger, registry=registry)
        registry.register("app", app)

        logger.info("Bootstrap complete.")
        return app
