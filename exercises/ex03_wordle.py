"""This program is a game where the user guesses the secret word. If a letter they guessed is in the word and in the right place, a green box will appear there. If it is in the word but not in the right spot, a yellow box will appear. If the letter isn't in the word, it'll be a white box."""

__author__ = "730770540"


def input_guess(secret_word_len: int) -> str:
    """This function asks the user to guess a word that is a certain number of characters long."""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    # Figuring out how to do the f-string template instead of using concatenation stumped me for a while- I now know it's just f'text' with any
    # ints being in {}.
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """This function determines if a singular character is found in the secret word."""
    # At first I was confused because just returning true whenever the char_guess is found in the secret_word isn't very indicative of where it
    # is located or how many times, but I later realized that would be figured out later in the code.
    assert len(char_guess) == 1
    count: int = 0
    while count < len(secret_word):
        if secret_word[count] == char_guess:
            return True
        else:
            count = count + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """This function creates a string of emojis, each coded to mean something else pertaining to if each character in the user's guessed word is found in the secret word, and if it's at the right placement in the word. Green = correct placement and is in word. Yellow = wrong placement but it is in the word. White = Not found in word."""
    assert len(guess) == len(secret)
    index: int = 0
    result: str = ""
    # It took me a while to realize I had to make a variable for "result" (as I called it), and almost made an empty list multiple times until I
    #  remembered an empty string exists.
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(secret):
        if guess[index] == secret[index]:
            result = result + GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]) == True:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        index = index + 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won: int = 0
    # I finally figured out this way of the program working with "won" being an int, but I kept attempting to make it a bool, and wasn't sure how
    #  to go about that.
    while turn <= 6 and won == 0:
        # I originally put my "guess" variable outside of the while-loop, and the program wouldn't ask for any other guesses and the user (me)
        # would lose- this makes more sense.
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        # The main function took me the longest because I had to figure out what the arguments for each function should be.
        print(emojified(guess=guess, secret=secret))
        if secret == guess:
            won = 1
            print(f"You won in {turn}/6 turns!")
        else:
            turn = turn + 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
