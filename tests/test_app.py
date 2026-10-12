import pytest

from src.app import add, divide, grade, is_palindrome


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


@pytest.mark.parametrize(
    "text, expected",
    [("Racecar", True), ("A man, a plan, a canal: Panama", True), ("hello", False)],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


@pytest.mark.parametrize(
    "score, expected",
    [(95, "A"), (85, "B"), (75, "C"), (65, "D"), (10, "F")],
)
def test_grade(score, expected):
    assert grade(score) == expected


@pytest.mark.parametrize("bad", [-1, 101])
def test_grade_out_of_range(bad):
    with pytest.raises(ValueError):
        grade(bad)
