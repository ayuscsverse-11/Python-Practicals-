"""Practical 7: Cubes of only the even integers in a list."""

# Enter a Python list, e.g. [1, 2, 3, 4, 'a', 6.0]
items = eval(input("Enter a list: "))

# 7(a) Using a for loop (bool is excluded because bool is a subclass of int)
cubes_loop = []
for item in items:
    if type(item) is int and item % 2 == 0:
        cubes_loop.append(item ** 3)
print("Using for loop:", cubes_loop)

# 7(b) Using list comprehension
cubes_comprehension = [
    item ** 3 for item in items
    if type(item) is int and item % 2 == 0
]
print("Using list comprehension:", cubes_comprehension)
