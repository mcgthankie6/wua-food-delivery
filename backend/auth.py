
"""User authentication module for WUA Food Delivery."""

import hashlib
import hmac
import os
import re


def hash_password(password):
    """Hash a password with a random salt using PBKDF2-SHA256."""
    if not isinstance(password, str) or not password:
        raise ValueError("A password is required.")

    salt = os.urandom(16)
    iterations = 600_000

    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations
    )

    return f"pbkdf2_sha256${iterations}${salt.hex()}${digest.hex()}"


def verify_password(password, stored_hash):
    """Check a password against its stored salted hash."""
    try:
        algorithm, count, salt_hex, digest_hex = stored_hash.split("$")
        if algorithm != "pbkdf2_sha256":
            return False

        expected = bytes.fromhex(digest_hex)
        actual = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(salt_hex),
            int(count)
        )

        return hmac.compare_digest(actual, expected)
    except (ValueError, TypeError, AttributeError):
        return False


def register_user(name, email, student_id, password):
    """Validate registration details and return a safe user record."""
    if not all([name, email, student_id, password]):
        raise ValueError("All fields are required.")

    if not isinstance(email, str) or not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+", email
    ):
        raise ValueError("Invalid email address.")

    return {
        "name": name,
        "email": email,
        "student_id": student_id,
        "password_hash": hash_password(password),
    }


def login_user(email, password):
    """Validate login inputs.

    Actual authentication requires retrieving a stored password hash
    and checking it with verify_password().
    """
    if not email or not password:
        raise ValueError("Email and password are required.")

    return False
