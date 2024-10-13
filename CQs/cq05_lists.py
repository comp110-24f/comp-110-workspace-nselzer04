"""Mutating functions."""

__author__ = "730770540"


def manual_append(a: list[int], b: int) -> None:
    """This function adds an integer onto the end of a list of integers."""
    a.append(b)


def double(a: list[int]) -> None:
    """This function doubles every object in the list a."""
    index: int = 0
    while index < len(a):
        a[index] = a[index] * 2
        index = index + 1


list_1: list[int] = [1, 2, 3]

list_2: list[int] = list_1

double(a=list_2)
print(list_1)
print(list_2)
