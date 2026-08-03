import uuid
from datetime import datetime, timezone
from src.core.logger import get_logger
from src.shared.models import Order, Signal
from src.shared.enums import OrderType, OrderStatus, OrderSide, SignalType
from src.execution.exceptions import OrderExecutionFailedError

logger = get_logger("ExecutionEngine")


class ExecutionEngine:
    """Executes trades based on risk-approved parameters. Never predicts market."""

    def execute_signal(self, signal: Signal, position_size: float) -> Order:
        if signal.suggested_price is None or signal.suggested_price <= 0:
            raise OrderExecutionFailedError("Cannot execute signal without valid suggested price")

        side = OrderSide.BUY if signal.signal_type == SignalType.ENTER_LONG else OrderSide.SELL
        quantity = round(position_size / signal.suggested_price, 4)
        order_id = f"ORD-{uuid.uuid4().hex[:8].upper()}"

        logger.info(f"Executing {side.value} order for {signal.symbol}: {quantity} units @ ${signal.suggested_price}")

        # Simulated instant fill for production baseline
        return Order(
            order_id=order_id,
            symbol=signal.symbol,
            side=side,
            order_type=OrderType.LIMIT,
            price=signal.suggested_price,
            quantity=quantity,
            filled_quantity=quantity,
            average_price=signal.suggested_price,
            status=OrderStatus.FILLED,
            created_at=datetime.now(timezone.utc),
        )
