class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def validate_symbol(symbol: str):
    if not symbol or not symbol.isalnum():
        raise ValidationError("Invalid symbol format.")


def validate_side(side: str):
    if side not in ["BUY", "SELL"]:
        raise ValidationError("Side must be BUY or SELL.")


def validate_order_type(order_type: str):
    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValidationError("Order type must be MARKET, LIMIT, or STOP.")


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than 0.")


def validate_price(order_type: str, price):
    if order_type in ["LIMIT", "STOP"]:
        if price is None:
            raise ValidationError("Price is required for LIMIT and STOP orders.")
        if float(price) <= 0:
            raise ValidationError("Price must be greater than 0.")


def validate_stop_price(order_type: str, stop_price):
    if order_type == "STOP":
        if stop_price is None:
            raise ValidationError("stopPrice is required for STOP orders.")
        if float(stop_price) <= 0:
            raise ValidationError("stopPrice must be greater than 0.")
