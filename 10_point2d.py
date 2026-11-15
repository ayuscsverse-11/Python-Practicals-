"""Practical 10: Define a 2D point class and calculate distance."""

import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"({self.x}, {self.y})")

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


p1 = Point2D(float(input("Point 1 - x: ")), float(input("Point 1 - y: ")))
p2 = Point2D(float(input("Point 2 - x: ")), float(input("Point 2 - y: ")))

print("Point 1:", end=" ")
p1.display()
print("Point 2:", end=" ")
p2.display()
print("Distance:", p1.distance(p2))
