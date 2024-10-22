"""This program will implement some more practice with list functions."""

__author__ = "730770540"


def only_evens(my_list: list[int]) -> list[int]:
    even_list: list[int] = []
    for number in my_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def sub(my_list: list[int], start: int, end: int) -> list[int]:
    end_list: list[int] = []
    if len(my_list) == 0 or start >= len(my_list) or end < 0:
        return end_list
    if start < 0:
        start = 0
    if end >= len(my_list):
        end = len(my_list)
    for i in range(start, end):
        end_list.append(my_list[i])
    return end_list


def add_at_index(my_list: list[int], added_int: int, index_int: int) -> None:
    if index_int < 0 or index_int > len(my_list):
        raise IndexError
    my_list.append(0)
    for value in range(len(my_list) - 1, index_int, -1):
        my_list[value] = my_list[value - 1]
    my_list[index_int] = added_int
