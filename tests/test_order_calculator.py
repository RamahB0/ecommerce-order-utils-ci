import pytest

from src.order_calculator import (
    LineItem,
    order_subtotal,
    order_total,
    validate_delivery_status_transition,
)


def test_line_total():
    item = LineItem(sku="PROD-1", unit_price=10.0, qty=3)
    assert item.line_total() == 30.0


def test_line_total_rejects_zero_qty():
    item = LineItem(sku="PROD-1", unit_price=10.0, qty=0)
    with pytest.raises(ValueError):
        item.line_total()


def test_order_subtotal():
    items = [
        LineItem(sku="PROD-1", unit_price=10.0, qty=2),
        LineItem(sku="PROD-2", unit_price=5.5, qty=1),
    ]
    assert order_subtotal(items) == 25.5


def test_order_total_with_tax_and_shipping():
    items = [LineItem(sku="PROD-1", unit_price=100.0, qty=1)]
    total = order_total(items, tax_rate=0.08, shipping=5.0)
    assert total == 113.0


def test_order_total_rejects_negative_tax():
    items = [LineItem(sku="PROD-1", unit_price=10.0, qty=1)]
    with pytest.raises(ValueError):
        order_total(items, tax_rate=-0.1)


@pytest.mark.parametrize(
    "current,new,expected",
    [
        ("pending", "confirmed", True),
        ("pending", "shipped", False),
        ("confirmed", "shipped", True),
        ("shipped", "delivered", True),
        ("delivered", "shipped", False),
        ("cancelled", "confirmed", False),
    ],
)
def test_delivery_status_transitions(current, new, expected):
    assert validate_delivery_status_transition(current, new) is expected
