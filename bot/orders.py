import logging
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.client import BinanceFuturesClient
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    ValidationError
)

logger = logging.getLogger(__name__)


def execute_order(symbol, side, order_type, quantity, price=None):
    """
    High-level order execution logic.
    Handles validation, API call, and response formatting.
    """

    try:
        # 1️⃣ Validate Inputs
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)

        logger.info("All inputs validated successfully.")

        # 2️⃣ Initialize Client
        client = BinanceFuturesClient()

        # 3️⃣ Place Order
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        # 4️⃣ Format Clean Output
        formatted_response = {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "symbol": response.get("symbol"),
            "side": response.get("side"),
            "type": response.get("type"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice"),
        }

        logger.info("Order executed successfully.")

        return formatted_response

    except ValidationError as ve:
        logger.error(f"Validation error: {str(ve)}")
        return {"error": f"Validation Error: {str(ve)}"}

    except BinanceAPIException as be:
        logger.error(f"Binance API error: {be.message}")
        return {"error": f"Binance API Error: {be.message}"}

    except BinanceRequestException as bre:
        logger.error(f"Binance request error: {str(bre)}")
        return {"error": f"Request Error: {str(bre)}"}

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {"error": f"Unexpected Error: {str(e)}"}
