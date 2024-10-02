"""Basic syntax of lists"""

my_numbers: list[float] = []  # literal

my_numbers: list[float] = []  # constructor

print(my_numbers)

# string analogy

# my_name: str = "" # literal

# my_name: str = str() # constructor

game_points: list[int] = [102, 86, 94]
print(game_points)

print(game_points[2])

print(["hello", "what", "hi"][1])

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(y[0])
