from dataclasses import dataclass
from src.shared.models import Signal, Account
from src.shared.enums import SignalType
from src.core.logger import get_logger

logger = get_logger("RiskEngine")


@dataclass(slots=True, frozen=True)
class RiskAssessment:
    is_approved: bool
    reason: str
    recommended_position_size: float = 0.0


class RiskEngine:
    """Highest priority evaluation engine. Validates and can reject any trading signal."""

    def __init__(
        self, max_risk_per_trade_pct: float = 0.02, max_leverage: int = 5
    ) -> None:
        self.max_risk_per_trade_pct = max_risk_per_trade_pct
        self.max_leverage = max_leverage

    def evaluate_signal(self, signal: Signal, account: Account) -> RiskAssessment:
        if signal.signal_type == SignalType.NO_SIGNAL:
            return RiskAssessment(is_approved=False, reason="NO_SIGNAL provided")

        if signal.strength < 0.5:
            logger.warning(
                f"Signal rejected for {signal.symbol}: Strength ({signal.strength}) below minimum threshold 0.5"
            )
            return RiskAssessment(
                is_approved=False,
                reason=f"Signal strength too low ({signal.strength})",
            )

        if account.available_balance <= 0:
            logger.warning(f"Signal rejected: Insufficient account balance ({account.available_balance})")
            return RiskAssessment(
                is_approved=False, reason="Insufficient available account balance"
            )

        # Calculate position size based on max risk percentage
        max_capital = account.available_balance * self.max_risk_per_trade_pct
        position_size = max_capital * self.max_leverage

        logger.info(f"Risk Check PASSED for {signal.symbol}. Approved position size: ${position_size:.2f}")
        return RiskAssessment(
            is_approved=True,
            reason="Risk rules satisfied",
            recommended_position_size=round(position_size, 2),
        )
