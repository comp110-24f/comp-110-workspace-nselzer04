"""This program will implement some more practice with list functions."""

__author__ = "730770540"


def only_evens(my_list: list[int]) -> list[int]:
    """This function returns a list that contains only the even integers from the given input list."""
    even_list: list[int] = []
    for number in my_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def sub(my_list: list[int], start: int, end: int) -> list[int]:
    """This function returns a list that contains integers from the input list, starting at the given starting index input, and ending before the ending index input."""
    end_list: list[int] = []
    if (
        len(my_list) == 0 or start >= len(my_list) or end < 0
    ):  # I accidentally wrote "or end <= 0", forgetting that 0 is still an index, and for this condition to work, it has to be for numbers smaller than zero.
        return end_list
    # How exactly to word all of the "exceptions" or unusual conditions confused me at first, and took me some time, as I at first tried to put them all within one while/for-loop/if-statement... This finally actually works.
    if start < 0:
        start = 0
    if end >= len(my_list):
        end = len(my_list)
    for i in range(
        start, end
    ):  # Not "end - 1" because for-in loops do not include the ending number in the range.
        end_list.append(my_list[i])
    return end_list


def add_at_index(my_list: list[int], added_int: int, index_int: int) -> None:
    """This function adds an input integer into a given input list at a certain given index, shifting the rest of the following numbers down, or to the right in the list."""
    if index_int < 0 or index_int > len(my_list):
        raise IndexError
    my_list.append(0)
    # This append becomes a place holder so that when I get rid of the last value off of the list after shifting it to the right, it's just this useless added value, not one that actually matters.
    for value in range(len(my_list) - 1, index_int, -1):
        # This took me a long while, and lots of googling on how python lists work- I did not know that one could iterate through a list backwards, however it makes a lot of sense since the final integer shows the "steps" each value takes when iterating through that list, and it could be -1 as shown.
        my_list[value] = my_list[value - 1]
    my_list[index_int] = added_int
