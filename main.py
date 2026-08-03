from src.core.bootstrap import Bootstrap
from src.automation.coordinator import AutomationCoordinator
from src.shared.enums import Timeframe


def main() -> None:
    app = Bootstrap().build()
    coordinator = AutomationCoordinator()
    
    try:
        app.run()
        # Trigger an automated cycle for BTC/USDT
        coordinator.run_pipeline("BTC/USDT", Timeframe.H1)
    finally:
        coordinator.close()
        app.shutdown()


if __name__ == "__main__":
    main()
