import pytest
from app.strength import score_password


def test_score_boundary_length_8():
    # edge case: exactly at the minimum length
    assert score_password("abcdefg") == 0
    assert score_password("abcdefgh") == 1


def test_score_non_string_raises():
    # invalid input
    with pytest.raises(TypeError):
        score_password(12345)
