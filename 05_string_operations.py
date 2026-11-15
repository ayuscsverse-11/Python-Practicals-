"""Practical 5: String operations."""

# 5(a) Frequency of a character in a string
text = input("Enter a string: ")
ch = input("Enter the character to count: ")
print("Frequency:", text.count(ch))


# 5(b) Replace a character with another character
text = input("\nEnter a string: ")
old = input("Character to replace: ")
new = input("Replacement character: ")
print("Updated string:", text.replace(old, new))


# 5(c) Remove the first occurrence of a character
text = input("\nEnter a string: ")
ch = input("Character to remove once: ")
position = text.find(ch)
if position == -1:
    print("Character not found:", text)
else:
    print("Updated string:", text[:position] + text[position + 1:])


# 5(d) Remove all occurrences of a character
text = input("\nEnter a string: ")
ch = input("Character to remove everywhere: ")
print("Updated string:", text.replace(ch, ""))


# 5(e) Swap the first n characters of two strings
s1 = input("\nEnter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter n: "))

if n < 0 or n > len(s1) or n > len(s2):
    print("n must be between 0 and the length of both strings.")
else:
    swapped1 = s2[:n] + s1[n:]
    swapped2 = s1[:n] + s2[n:]
    print("First string after swapping:", swapped1)
    print("Second string after swapping:", swapped2)
