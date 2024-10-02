"""This program imports and runs functions from other files, to print the coordinates of both input words."""

__author__ = "730770540"

from CQs.cq04.concatenation import concat

x: str = "123"

y: str = "abc"

print(concat(x, y))


from CQs.cq04.coordinates import get_coords

print(get_coords(x, y))
