"""This program practices creating/using functions with dictionaries."""

__author__ = "730770540"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """This function takes a list and inverts the keys and values of that list."""
    end_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in end_dict:
            # It took me a while to figure out that you could do this "input_dict[key] in end_dict" line, because I thought you could only do
            # "key in end_dict", which wouldn't have allowed this function to work.
            raise KeyError("Duplicate value found.")
        end_dict[input_dict[key]] = key
    return end_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """This function determines the color that the most people said was their favorite."""
    color_count: dict[str, int] = {}
    first: list[str] = []
    # Getting this function started took me a long time because I didn't know whether I needed to even create what would be max_count or if I had
    # to make another empty string in order to determine which string was first and therefore which one to return if they were equal.
    for key in input_dict:
        if input_dict[key] in color_count:
            color_count[input_dict[key]] += 1
            # I didn't make an if/else statement at first and just made color_count[input_dict[key]] +=1, which didn't work so I broke it down,
            # which makes sense because with my original way I didn't actually initialize that key to equal anything.
        else:
            color_count[input_dict[key]] = 1
            first.append(input_dict[key])
    most_freq_color: str = ""
    max_count: int = 0
    for color in first:
        if color_count[color] > max_count:
            max_count = color_count[color]
            most_freq_color = color
    return most_freq_color


def count(input_list: list[str]) -> dict[str, int]:
    """This function returns a dictionary with the input values and the number of times each appeared in the input list."""
    end_dict: dict[str, int] = {}
    for value in input_list:
        if value in end_dict:
            end_dict[value] += 1
        else:
            end_dict[value] = 1
    return end_dict


def alphabetizer(input_list: [list[str]]) -> dict[str, list[str]]:
    """This function returned the input strings as values to the key, which is the (lowercase) letter that the word begins with."""
    result_dict: dict[str, list[str]] = {}
    for value in input_list:
        # I could not figure out how to use the ".lower" at first, but now realize that making it the value of a new variable makes the most sense.
        lower: str = value[0].lower()
        if lower in result_dict:
            result_dict[lower].append(value)
            # I could not figure out how to add an object to a list that is the value in a dictionary- I first made an empty list and kept having
            # the dict_name[key] = list.append(value), which did not work because this is actually the way to append values to lists.
        else:
            result_dict[lower] = []
            result_dict[lower].append(value)
    return result_dict


def update_attendance(
    attendance_log: dict[str, list[str]], day_of_week: str, student_attended: str
) -> None:
    """This function updates the attendance log by adding the names of students in attendance (the value) to each day of the week (which was the key.)"""
    if day_of_week in attendance_log:
        attendance_log[day_of_week].append(student_attended)
    else:
        attendance_log[day_of_week] = []
        attendance_log[day_of_week].append(student_attended)
