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
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValidationError("Order type must be MARKET or LIMIT.")


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than 0.")


def validate_price(order_type: str, price):
    if order_type == "LIMIT":
        if price is None:
            raise ValidationError("Price is required for LIMIT orders.")
        if float(price) <= 0:
            raise ValidationError("Price must be greater than 0.")
