import pytest

from src.common_password import is_common


def test_common_password_is_detected():
    assert is_common("password") is True


def test_uncommon_password_is_accepted():
    assert is_common("T7#kLq9!vZx2") is False


def test_is_common_ignores_case_and_spaces():
    assert is_common("  PassWord  ") is True


def test_empty_string_is_not_common():
    assert is_common("") is False


def test_non_string_input_raises_error():
    with pytest.raises(TypeError):
        is_common(12345)
