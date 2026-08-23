"""Small order-calculation utilities, pulled out of the e-commerce NoSQL
order schema so they can be exercised with real unit tests, linting, and CI.
"""

from dataclasses import dataclass


@dataclass
class LineItem:
    sku: str
    unit_price: float
    qty: int

    def line_total(self) -> float:
        if self.qty < 1:
            raise ValueError("qty must be at least 1")
        return round(self.unit_price * self.qty, 2)


def order_subtotal(items):
    """Sum the line totals for a list of LineItem."""
    return round(sum(item.line_total() for item in items), 2)


def order_total(items, tax_rate=0.0, shipping=0.0):
    """Compute subtotal + tax + shipping."""
    if tax_rate < 0:
        raise ValueError("tax_rate cannot be negative")
    subtotal = order_subtotal(items)
    tax = round(subtotal * tax_rate, 2)
    return round(subtotal + tax + shipping, 2)


ALLOWED_STATUS_TRANSITIONS = {
    "pending": {"confirmed", "cancelled"},
    "confirmed": {"shipped", "cancelled"},
    "shipped": {"delivered"},
    "delivered": set(),
    "cancelled": set(),
}


def validate_delivery_status_transition(current, new):
    """Return True if the delivery status transition is allowed."""
    return new in ALLOWED_STATUS_TRANSITIONS.get(current, set())
