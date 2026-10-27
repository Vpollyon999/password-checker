from app.password_checker import validate_password_length


def test_password_meets_minimum_length():
    assert validate_password_length("Password123") is True


def test_password_too_short():
    assert validate_password_length("abc") is False