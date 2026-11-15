"""Practical 13: Tuple operations."""

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# 13(a) Print half the values on each line
middle = len(t1) // 2
print("First half:", *t1[:middle])
print("Second half:", *t1[middle:])

# 13(b) Create another tuple containing even values
even_tuple = tuple(value for value in t1 if value % 2 == 0)
print("\nEven values:", even_tuple)

# 13(c) Concatenate with another tuple
t2 = (11, 13, 15)
combined = t1 + t2
print("Concatenated tuple:", combined)

# 13(d) Maximum and minimum
print("Maximum:", max(combined))
print("Minimum:", min(combined))
