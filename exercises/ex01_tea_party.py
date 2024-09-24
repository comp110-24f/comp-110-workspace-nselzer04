"""Plans how many tea bags and treats are needed for a tea party based on the
user's input of how many guests will attend, and determines the cost of the 
party."""

__author__: str = "730770540"


def main_planner(guests: int) -> None:
    """Calls and prints the other functions."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    # Kept forgetting to change certain types into other types- like in this
    # function, every int/float had to be converted into strings to be
    # concatenated with other strings.
    print("Treats: " + str(treats(people=guests)))
    # Needed to add tea_count = tea_bags... and treat_count = treats... as
    # variables here because without it, this function body would be using
    # parameters within the 15th line that aren't defined, so an error would
    # occur.
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Determines the total # of teabags needed based on the # of people."""
    return 2 * people


def treats(people: int) -> int:
    """Determines the total # of treats needed based on the # of tea bags, based on the # of people."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determines the cost based on the # of tea bags and treats needed."""
    # I had to break this whole function body down into more parts (adding cost_per_tea_bag and cost_per_treat, and then
    # tea_cost, etc. because simply writing: return (tea_count * .50) + (treat_count * .75) resulted in an error stating that
    # operation did not work, so I thought breaking it down would help me see where things went wrong- however the broken down
    # version actually worked and I left it. I think either way works; I must've just made a script error the first time.
    #  Nevermind, I changed it back because the autograder said to.
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many quests are attending your tea party? ")))
