from bot.client import BinanceFuturesClient

client = BinanceFuturesClient()

response = client.place_order(
    symbol="BTCUSDT",
    side="BUY",
    order_type="MARKET",
    quantity=0.004
)

print(response)
