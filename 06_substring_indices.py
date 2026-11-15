"""Practical 6: Find all indices where the second string occurs in the first."""


def find_all_occurrences(first, second):
    if second == "":
        return -1
    indices = []
    start = 0
    while True:
        index = first.find(second, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1  # +1 also finds overlapping occurrences
    return indices if indices else -1


first = input("Enter the first string: ")
second = input("Enter the second string: ")
print("Indices:", find_all_occurrences(first, second))
