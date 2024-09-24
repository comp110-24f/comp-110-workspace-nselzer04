"""This program practices iterating through a string with a while loop, by determining the number of times a certain character can be found in a phrase."""

__author__ = "730770540"


def num_instances(phrase: str, search_char: str) -> int:
    """This function returns the number of times that the single character of search_char is found in phrase."""
    count: int = 0
    track: int = 0
    while track < len(phrase):
        if phrase[track] == search_char:
            count = count + 1
        track = track + 1
    return count
