from enum import Enum, auto
from typing import Callable, List
from src.core.logger import get_logger

logger = get_logger("LifecycleManager")


class LifecycleState(Enum):
    CREATED = auto()
    STARTING = auto()
    RUNNING = auto()
    STOPPING = auto()
    STOPPED = auto()


class LifecycleManager:
    """Manages application states and executes registered startup/shutdown hooks."""

    def __init__(self) -> None:
        self.state: LifecycleState = LifecycleState.CREATED
        self._startup_hooks: List[Callable[[], None]] = []
        self._shutdown_hooks: List[Callable[[], None]] = []

    def add_startup_hook(self, hook: Callable[[], None]) -> None:
        self._startup_hooks.append(hook)

    def add_shutdown_hook(self, hook: Callable[[], None]) -> None:
        self._shutdown_hooks.append(hook)

    def start(self) -> None:
        self.state = LifecycleState.STARTING
        logger.info("Executing startup hooks...")
        for hook in self._startup_hooks:
            hook()
        self.state = LifecycleState.RUNNING
        logger.info("Lifecycle state changed to RUNNING")

    def stop(self) -> None:
        self.state = LifecycleState.STOPPING
        logger.info("Executing shutdown hooks...")
        for hook in self._shutdown_hooks:
            hook()
        self.state = LifecycleState.STOPPED
        logger.info("Lifecycle state changed to STOPPED")
