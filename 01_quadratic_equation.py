"""Practical 1: Find the roots of a quadratic equation."""

import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
else:
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
