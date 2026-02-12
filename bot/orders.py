import logging
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.client import BinanceFuturesClient
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_stop_price,
    ValidationError
)

logger = logging.getLogger(__name__)

def execute_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    """
    High-level order execution logic.
    Handles validation, API call, and response formatting.
    """

    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)

        logger.info("All inputs validated successfully.")

        client = BinanceFuturesClient()

        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        if "orderId" in response:
            formatted_response = {
                "orderId": response.get("orderId"),
                "status": response.get("status"),
                "symbol": response.get("symbol"),
                "side": response.get("side"),
                "type": response.get("type"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice"),
            }
        elif "algoId" in response:
            formatted_response = {
                "orderId": response.get("algoId"),
                "status": response.get("algoStatus"),
                "symbol": response.get("symbol"),
                "side": response.get("side"),
                "type": response.get("orderType"),
                "executedQty": "0",
                "avgPrice": "0",
            }
        else:
            formatted_response = {"error": "Unknown response format received from Binance."}

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
