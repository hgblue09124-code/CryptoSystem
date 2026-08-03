from typing import Any, Dict
from src.core.exceptions import ServiceNotFoundError


class ServiceRegistry:
    """Central registry for application dependency injection."""

    def __init__(self) -> None:
        self._services: Dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        if name in self._services:
            raise KeyError(f"Service '{name}' is already registered.")
        self._services[name] = service

    def get(self, name: str) -> Any:
        if name not in self._services:
            raise ServiceNotFoundError(f"Service '{name}' not found in registry.")
        return self._services[name]
