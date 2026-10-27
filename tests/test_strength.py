import pytest
from app.strength import score_password, strength_label, get_feedback


def test_score_boundary_length_8():
    # edge case: exactly at the minimum length
    assert score_password("abcdefg") == 0
    assert score_password("abcdefgh") == 1


def test_score_non_string_raises():
    # invalid input
    with pytest.raises(TypeError):
        score_password(12345)


def test_weak_password():
    # normal behavior
    assert strength_label("abc") == "weak"


def test_medium_password():
    assert strength_label("Abcdefg1") == "medium"


def test_strong_password():
    assert strength_label("Str0ng!Passw0rd") == "strong"


def test_empty_password_is_weak():
    # edge case: empty string
    assert strength_label("") == "weak"


def test_feedback_for_weak_password():
    # normal behavior: every rule is missing
    assert len(get_feedback("abc")) == 4


def test_feedback_for_strong_password_is_empty():
    # edge case: nothing to improve
    assert get_feedback("Str0ng!Passw0rd") == []


def test_feedback_non_string_raises():
    # invalid input
    with pytest.raises(TypeError):
        get_feedback(None)
