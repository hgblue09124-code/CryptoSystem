# Đổi import từ MockClient sang ScexClient
from src.collector.scex_client import ScexExchangeClient
from src.collector.service import CollectorService

class Container:
    def __init__(self):
        # Sử dụng ScexExchangeClient thay cho MockExchangeClient
        self.exchange_client = ScexExchangeClient()
        self.collector_service = CollectorService(exchange_client=self.exchange_client)