from app.password_checker import validate_password_length


def test_password_meets_minimum_length():
    assert validate_password_length("Password123") is True


def test_password_too_short():
    assert validate_password_length("abc") is False
def test_empty_password():
    assert validate_password_length("") is False


def test_password_one_character():
    assert validate_password_length("a") is False


def test_password_at_minimum_length():
    assert validate_password_length("Password1") is True


def test_long_password():
    assert validate_password_length("ThisIsAVeryLongPassword123") is True