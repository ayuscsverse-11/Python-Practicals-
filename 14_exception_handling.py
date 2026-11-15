"""Practical 14: Accept a name and raise/handle exceptions for digits or special characters."""


class InvalidNameError(Exception):
    pass


try:
    name = input("Enter your name: ").strip()

    if not name:
        raise InvalidNameError("Name cannot be empty.")

    # Allow alphabetic characters and spaces only
    if not all(character.isalpha() or character.isspace() for character in name):
        raise InvalidNameError(
            "Name must not contain digits or special characters."
        )

    print("Valid name:", name)

except InvalidNameError as error:
    print("Invalid name:", error)
