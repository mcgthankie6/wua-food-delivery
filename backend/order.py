
"""Order tracking functionality for WUA Food Delivery."""


class Order:
    """Represent a student's food order."""

    def __init__(self, order_id, student_id, items,
                 total_price, status="Pending"):
        self.order_id = order_id
        self.student_id = student_id
        self.items = items
        self.total_price = total_price
        self.status = status


# Temporary in-memory storage for orders
ORDERS = {}


def update_order_status(order_id, new_status):
    """Update the status of an existing order."""

    if order_id not in ORDERS:
        raise ValueError("Order not found.")

    allowed_statuses = {
        "Pending",
        "Preparing",
        "Ready",
        "Collected",
        "Cancelled"
    }

    if new_status not in allowed_statuses:
        raise ValueError("Invalid order status.")

    ORDERS[order_id].status = new_status

    return ORDERS[order_id]
