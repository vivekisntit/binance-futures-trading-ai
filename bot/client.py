import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot import API_KEY, API_SECRET

logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    def __init__(self):
        if not API_KEY or not API_SECRET:
            raise ValueError("API credentials not found. Check your .env file.")

        self.client = Client(API_KEY, API_SECRET)

        # Override to use Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Binance Futures Testnet client initialized.")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(f"Placing order: {symbol} | {side} | {order_type} | Qty: {quantity} | Price: {price}")

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.futures_create_order(**params)

            logger.info(f"Order response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Binance request error: {str(e)}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise
