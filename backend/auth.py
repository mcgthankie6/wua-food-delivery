
"""Authentication functions for WUA Food Delivery."""


def register_user(name, email, student_id, password):
    """Register a user after checking that all fields are provided."""
    if not all([name, email, student_id, password]):
        raise ValueError("All fields are required.")

    return {
        "name": name,
        "email": email,
        "student_id": student_id,
        "password": password,
    }


def login_user(email, password):
    """Validate that login credentials have been provided."""
    if not email or not password:
        raise ValueError("Email and password are required.")

    # Actual login verification requires stored user records.
    return False
