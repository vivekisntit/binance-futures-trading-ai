import logging
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.handlers = []

    file_handler = logging.FileHandler("logs/trading_bot.log")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    )

    logger.addHandler(file_handler)

    api_logger = logging.getLogger("api_logger")
    api_logger.setLevel(logging.INFO)

    api_handler = logging.FileHandler("logs/api_responses.log")
    api_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(message)s")
    )

    api_logger.addHandler(api_handler)
    api_logger.propagate = False
