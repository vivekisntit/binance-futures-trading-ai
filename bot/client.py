import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot import API_KEY, API_SECRET

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self):
        if not API_KEY or not API_SECRET:
            raise ValueError("API credentials not found. Check your .env file.")

        # Initialize the client specifically for Testnet
        # This automatically sets the correct URLs for you
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        
        # Explicitly remove the manual URL overrides you had. 
        # The library handles this when testnet=True.
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
