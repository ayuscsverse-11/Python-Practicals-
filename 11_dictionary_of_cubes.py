"""Practical 11: Dictionary with numbers 1 to 5 and their cubes."""


def cube_dictionary():
    return {number: number**3 for number in range(1, 6)}


print(cube_dictionary())
