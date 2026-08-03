from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from src.shared.enums import (
    Timeframe,
    OrderSide,
    OrderType,
    OrderStatus,
    PositionSide,
    SignalType,
)
from src.shared.exceptions import ValidationError


@dataclass(slots=True, frozen=True)
class Candle:
    symbol: str
    timeframe: Timeframe
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    def __post_init__(self) -> None:
        if self.high < max(self.open, self.close, self.low):
            raise ValidationError(f"Invalid Candle high price for {self.symbol}")
        if self.low > min(self.open, self.close, self.high):
            raise ValidationError(f"Invalid Candle low price for {self.symbol}")
        if self.volume < 0:
            raise ValidationError(f"Volume cannot be negative for {self.symbol}")


@dataclass(slots=True, frozen=True)
class Ticker:
    symbol: str
    bid: float
    ask: float
    last: float
    volume_24h: float
    timestamp: datetime

    def __post_init__(self) -> None:
        if self.bid > self.ask:
            raise ValidationError(f"Bid ({self.bid}) cannot be greater than Ask ({self.ask}) for {self.symbol}")


@dataclass(slots=True, frozen=True)
class Signal:
    symbol: str
    signal_type: SignalType
    strength: float
    timestamp: datetime
    source_strategy: str
    suggested_price: Optional[float] = None

    def __post_init__(self) -> None:
        if not (0.0 <= self.strength <= 1.0):
            raise ValidationError("Signal strength must be between 0.0 and 1.0")


@dataclass(slots=True, frozen=True)
class Order:
    order_id: str
    symbol: str
    side: OrderSide
    order_type: OrderType
    price: float
    quantity: float
    status: OrderStatus
    created_at: datetime
    filled_quantity: float = 0.0
    average_price: float = 0.0


@dataclass(slots=True, frozen=True)
class Position:
    symbol: str
    side: PositionSide
    entry_price: float
    quantity: float
    leverage: int
    unrealized_pnl: float
    liquidation_price: Optional[float] = None


@dataclass(slots=True, frozen=True)
class Account:
    account_id: str
    total_balance: float
    available_balance: float
    currency: str = "USDT"
