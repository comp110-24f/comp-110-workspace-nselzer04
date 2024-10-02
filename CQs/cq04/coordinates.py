"""This program gets the coordinates of each character of the inputs."""

__author__ = "730770540"


def get_coords(xs: str, ys: str) -> None:
    """This function prints the pairs of each character of the input."""
    count_xs: int = 0
    count_ys: int = 0
    while count_xs < len(xs):
        while count_ys < len(ys):
            print("(" + xs[count_xs] + ", " + ys[count_ys] + ")")
            count_ys = count_ys + 1
        count_xs = count_xs + 1
        count_ys = 0
