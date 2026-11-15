"""Practical 8: Read a file and perform file operations."""

# Create a sample input file (replace with your own file if you like)
sample_text = """Python is easy to learn.
Python is a popular programming language.
File handling is useful."""

with open("input.txt", "w", encoding="utf-8") as file:
    file.write(sample_text)

input_filename = "input.txt"

# Read file contents
with open(input_filename, "r", encoding="utf-8") as file:
    content = file.read()

# 8(a) Total number of characters, words and lines
character_count = len(content)
word_count = len(content.split())
line_count = len(content.splitlines())

print("Characters:", character_count)
print("Words:", word_count)
print("Lines:", line_count)

# 8(b) Frequency of each character using a dictionary
frequency = {}
for character in content:
    frequency[character] = frequency.get(character, 0) + 1
print("\nCharacter frequencies:")
print(frequency)

# 8(c) Print words in reverse order
words = content.split()
print("\nWords in reverse order:")
print(" ".join(words[::-1]))

# 8(d) Copy even-numbered lines to File1 and odd-numbered lines to File2
lines = content.splitlines(keepends=True)
with open("File1", "w", encoding="utf-8") as even_file, \
        open("File2", "w", encoding="utf-8") as odd_file:
    for line_number, line in enumerate(lines, start=1):
        if line_number % 2 == 0:
            even_file.write(line)
        else:
            odd_file.write(line)

print("\nCreated File1 (even lines) and File2 (odd lines).")
