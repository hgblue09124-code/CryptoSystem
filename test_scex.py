import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.collector.scex_client import ScexExchangeClient

client = ScexExchangeClient()
trades = client.fetch_recent_trades("SBTC_VND")
candle = client.convert_trades_to_candle(trades)

print("=== GIÁ SCEX CẬP NHẬT REALTIME ===")
print(f"Giá khớp mới nhất: {client.get_latest_price():,.0f} VND")
print("\n=== THÔNG TIN NẾN TẠO TỪ SCEX ===")
print(candle)
