"""This program asks the user to guess a number, and tells them if they guessed it right, or if they were too low/high."""

__author__ = "730770540"


def guess_a_number() -> None:
    """This function asks the user to guess a number, and tells them if they guessed it right, or if they were too low/high."""
    secret: int = 7
    x: str = input("Guess a number: ")
    print("Your guess was " + x)
    if int(x) == secret:
        print("You got it!")
    elif int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
