from bot.orders import execute_order

response = execute_order(
    symbol="BTCUSDT",
    side="BUY",
    order_type="MARKET",
    quantity=0.004
)

print(response)
