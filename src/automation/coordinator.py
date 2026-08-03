from src.core.logger import get_logger
from src.shared.models import Account
from src.shared.enums import Timeframe
from src.database.connection import DatabaseConnection
from src.database.schema import SchemaManager
from src.database.repository import CandleRepository, OrderRepository
from src.collector.mock_client import MockExchangeClient
from src.collector.service import MarketCollectorService
from src.research.analyzer import MarketAnalyzer
from src.decision.strategy import RsiStrategy
from src.risk.rules import RiskEngine
from src.execution.executor import ExecutionEngine
from src.dashboard.view import SystemDashboard
from src.ai.advisor import AIAdvisor

logger = get_logger("AutomationCoordinator")


class AutomationCoordinator:
    """Coordinates end-to-end workflow execution. Ensures Risk Engine is NEVER bypassed."""

    def __init__(self, db_path: str = "data/cryptosystem.db") -> None:
        self.db_conn = DatabaseConnection(db_path)
        conn = self.db_conn.connect()
        
        # Initialize Schema & Repositories
        SchemaManager(conn).initialize_schema()
        self.candle_repo = CandleRepository(conn)
        self.order_repo = OrderRepository(conn)

        # Initialize Independent Modules
        self.collector = MarketCollectorService(MockExchangeClient(), self.candle_repo)
        self.analyzer = MarketAnalyzer()
        self.strategy = RsiStrategy()
        self.risk_engine = RiskEngine()
        self.execution_engine = ExecutionEngine()
        self.dashboard = SystemDashboard()
        self.ai_advisor = AIAdvisor()

    def run_pipeline(self, symbol: str, timeframe: Timeframe) -> None:
        logger.info(f"=== STARTING AUTOMATION CYCLE FOR {symbol} ===")
        
        # 1. Collect Data
        candles = self.collector.collect_and_store_candles(symbol, timeframe, limit=60)

        # 2. Research & Metrics Calculation
        metrics = self.analyzer.analyze_market(candles)

        # 3. AI Layer Recommendation (Optional context)
        ai_rec = self.ai_advisor.analyze_regime(metrics)
        logger.info(f"AI Advisor Confidence: {ai_rec.confidence_score} | {ai_rec.summary}")

        # 4. Decision Engine (Strategy)
        signal = self.strategy.evaluate(symbol, metrics)

        # Simulated Account
        account = Account(account_id="ACC-001", total_balance=10000.0, available_balance=10000.0)

        # 5. Risk Engine Verification (Mandatory Barrier)
        risk_assessment = self.risk_engine.evaluate_signal(signal, account)

        orders_history = []
        if risk_assessment.is_approved:
            # Apply AI multiplier cautiously to position size
            adjusted_position_size = risk_assessment.recommended_position_size * ai_rec.suggested_risk_multiplier

            # 6. Execution Engine
            order = self.execution_engine.execute_signal(signal, adjusted_position_size)
            self.order_repo.save_order(order)
            orders_history.append(order)
        else:
            logger.warning(f"Workflow halted by Risk Engine: {risk_assessment.reason}")

        # 7. Dashboard Reporting
        self.dashboard.render_summary(account, orders_history, metrics)
        logger.info("=== AUTOMATION CYCLE COMPLETED ===")

    def close(self) -> None:
        self.db_conn.close()
