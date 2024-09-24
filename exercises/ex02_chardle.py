"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730770540"


def input_word() -> str:
    """This function asks the user for a 5-letter word, stopping if they provide a word with less/more than 5 characters."""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """This function asks the user for a single letter, stopping if they provide more than a single character."""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """This function determines if (and where) the user's guessed letter is found in their word, and how many times it is found in the word."""
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        # Kept having an error because at first I tried to concatenate strings with integers (0 in this line.)
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + "found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """This function puts it all together, calling each function."""
    contains_char(word=input_word(), letter=input_letter())
    # I at first had an error with calling contains_char before I got to part 6 (putting everything together) because for the parameters, I just
    # used word and letter, without adding the equals input_word and equals input_letter, so essentially not telling the function where to get
    # the word and letter.


if __name__ == "__main__":
    main()
