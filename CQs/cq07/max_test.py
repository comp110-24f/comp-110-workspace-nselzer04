"""Testing find_and_remove_max."""

__author__ = "730770540"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return_use_case() -> None:
    """Testing find_and_remove_max returns the max value."""
    assert find_and_remove_max([6, 8, 9, 6, 9]) == 9


def test_find_and_remove_max_use_case() -> None:
    """Testing find_and_remove_max removes max value."""
    a: list[int] = [6, 8, 9, 6, 9]
    find_and_remove_max(a)
    assert a == [6, 8, 6]


def test_find_and_remove_max_return_val_use_case() -> None:
    """Testing find_and_remove_max returns -1 in an unconventional case (empty brackets.)"""
    assert find_and_remove_max([]) == -1
