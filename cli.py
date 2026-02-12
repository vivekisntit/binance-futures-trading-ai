import argparse
import logging

from bot.logging_config import setup_logging
from bot.orders import execute_order


def main():
    # Setup logging first
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side (BUY or SELL)")
    parser.add_argument("--type", required=True, help="Order type (MARKET or LIMIT)")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    logger.info("CLI arguments received.")

    print("\n===== Order Request Summary =====")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    if args.type.upper() == "LIMIT":
        print(f"Price: {args.price}")

    response = execute_order(
        symbol=args.symbol.upper(),
        side=args.side.upper(),
        order_type=args.type.upper(),
        quantity=args.quantity,
        price=args.price
    )

    print("\n===== Order Response =====")

    if "error" in response:
        print(response["error"])
    else:
        print("Order executed successfully!")
        print(f"Order ID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Executed Qty: {response['executedQty']}")
        print(f"Average Price: {response['avgPrice']}")

    print("\n===============================")


if __name__ == "__main__":
    main()
