"""First CQ!"""

__author__ = "730770540"


def mimic(message: str) -> str:
    """This function repeats your input back to you."""
    return message


def main() -> None:
    """Print message"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
