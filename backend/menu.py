
"""Menu browsing functionality for WUA Food Delivery."""

FOOD_ITEMS = {
    "Chicken and Rice": 5.00,
    "Beef Burger": 4.50,
    "Vegetable Pizza": 6.00,
    "Chips": 2.00,
    "Chicken Sandwich": 3.50,
}


def get_menu(cafeteria_name):
    """Return the food menu for the specified cafeteria."""
    if not cafeteria_name or not cafeteria_name.strip():
        raise ValueError("Cafeteria name is required.")

    return {
        "cafeteria": cafeteria_name,
        "items": FOOD_ITEMS.copy(),
    }
