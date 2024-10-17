"""This program practices using lists in different ways."""

__author__ = "730770540"


def all(the_list: list[int], the_int: int) -> bool:
    """This function will return "True" if a given int is the only int found in the given list, and "False" if not."""
    if len(the_list) == 0:
        return False
    for elem in the_list:
        # I had trouble with this, because I kept writing "for idx in the_list", and then trying to index, the_list[idx], and getting an error. I looked back at the slides in order to figure this out.
        if elem != the_int:
            return False
    return True


def max(input: list[int]) -> int:
    """This function returns the maximum number in the given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = input[0]
    for elem in input:
        if elem > max_num:
            max_num = elem
    return max_num


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """This function returns "True" if the given lists are fully equal to each other, but "False" otherwise."""
    if len(list_one) != len(list_two):
        return False
    for i in range(len(list_one)):
        # After indexing didn't work on the "all" function, this one confused me for a while- I had to look at the slides to realize I just needed to use the "for i in range..." loop instead of just "for i in list_one."
        if list_one[i] != list_two[i]:
            return False
    return True


def extend(a: list[int], b: list[int]) -> None:
    """This function adds the elements of the second list onto the first list."""
    for elem in b:
        a.append(elem)
