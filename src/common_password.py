COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "111111", "123123", "admin", "letmein",
    "welcome", "iloveyou", "monkey", "dragon", "football",
}


def is_common(pw):
    """Return True if the password is in the list of common passwords."""
    if not isinstance(pw, str):
        raise TypeError("Password must be a string")
    return pw.strip().lower() in COMMON_PASSWORDS
