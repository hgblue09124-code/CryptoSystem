from typing import List, Dict, Any
from src.core.logger import get_logger
from src.shared.models import Account, Order

logger = get_logger("DashboardView")


class SystemDashboard:
    """Provides pure visualization of system status, account balance, and execution history."""

    def render_summary(self, account: Account, recent_orders: List[Order], metrics: Dict[str, Any]) -> None:
        logger.info("--- CRYPTOSYSTEM TELEMETRY DASHBOARD ---")
        logger.info(f"Account Balance : ${account.total_balance:.2f} {account.currency} (Avail: ${account.available_balance:.2f})")
        logger.info(f"Market Metrics  : RSI: {metrics.get('rsi_14')}, Trend: {metrics.get('trend')}, Close: ${metrics.get('latest_close')}")
        logger.info(f"Executed Orders : {len(recent_orders)} orders in history")
        for order in recent_orders[-3:]:
            logger.info(f"  -> [{order.status.name}] {order.side.value} {order.quantity} {order.symbol} @ ${order.price}")
        logger.info("-----------------------------------------")
