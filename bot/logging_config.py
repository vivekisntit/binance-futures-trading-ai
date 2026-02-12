import logging
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)

    # Root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove default handlers (important)
    logger.handlers = []

    # File handler for concise app logs
    file_handler = logging.FileHandler("logs/trading_bot.log")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    )

    logger.addHandler(file_handler)

    # Dedicated logger for raw API responses
    api_logger = logging.getLogger("api_logger")
    api_logger.setLevel(logging.INFO)

    api_handler = logging.FileHandler("logs/api_responses.log")
    api_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(message)s")
    )

    api_logger.addHandler(api_handler)
    api_logger.propagate = False
