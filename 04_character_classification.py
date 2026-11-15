"""Practical 4: Character classification."""

ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
elif ch.isalpha():
    print("The character is a letter.")
    print("It is uppercase." if ch.isupper() else "It is lowercase.")
elif ch.isdigit():
    digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
                   "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    print("The character is a numeric digit.")
    print("Digit in words:", digit_names[int(ch)])
else:
    print("The character is a special character.")
