"""This program returns the concatenation of two inputs from the user."""

__author__ = "730770540"


def concat(input_one: str, input_two: str) -> str:
    """This function concatenates two input strings and returns this concatenation."""
    return input_one + input_two


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
