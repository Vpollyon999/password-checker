def validate_password_length(password):
    """Check that the password is not empty and has at least 8 characters."""
    if not password:
        return False

    return len(password) >= 8