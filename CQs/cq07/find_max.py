"""This program has a function that finds and returns the max value of a list, and also removes that value from the list."""

__author__ = "730770540"


def find_and_remove_max(a: list[int]) -> int:
    """This function finds and returns the max value of a list, and also removes that value from the list."""
    if a == []:
        return -1
    else:
        largest: int = a[0]
        for num in a:
            if num > largest:
                largest = num
        index: int = 0
        while index < len(a):
            if a[index] == largest:
                a.pop(index)
            else:
                index = index + 1
        return largest
