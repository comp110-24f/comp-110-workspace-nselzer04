"""This program will contain unit tests for the functions implemented in the utils.py file."""

__author__ = "730770540"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest


def test_only_evens_return_use_case() -> None:
    assert only_evens([3, 4, 7, 13, 14, 20, 22]) == [4, 14, 20, 22]


def test_only_evens_input_use_case() -> None:
    my_list: list[int] = [3, 4, 7, 13, 14, 20, 22]
    only_evens(my_list)
    assert my_list == [3, 4, 7, 13, 14, 20, 22]


def test_only_evens_edge_case() -> None:
    my_list: list[int] = []
    only_evens(my_list)
    assert my_list == []


def test_sub_return_use_case() -> None:
    assert sub([15, 25, 35, 45, 55, 65], 1, 4) == [25, 35, 45]


def test_sub_input_use_case() -> None:
    my_list: list[int] = [15, 25, 35, 45, 55, 65]
    sub(my_list, 1, 4)
    assert my_list == [15, 25, 35, 45, 55, 65]


def test_sub_edge_case() -> None:
    assert sub([15, 25, 35, 45, 55, 65], 8, 10) == []


def test_add_at_index_return_use_case() -> None:
    assert add_at_index([2, 4, 6, 8, 12, 14], 10, 4) == None


def test_add_at_index_input_use_case() -> None:
    my_list: list[int] = [2, 4, 6, 8, 12, 14]
    add_at_index(my_list, 10, 4)
    assert my_list == [2, 4, 6, 8, 10, 12, 14]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index([2, 4, 6, 8, 12, 14], 8, 10)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
