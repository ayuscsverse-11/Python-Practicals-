"""Practical 3: Print a pyramid and a reverse pyramid using '*'."""

rows = int(input("Enter number of rows: "))

print("Pyramid:")
for i in range(1, rows + 1):
    print("*" * (2*i - 1))

print("\nReverse pyramid:")
for i in range(rows, 0, -1):
    print("*" * (2*i - 1))
