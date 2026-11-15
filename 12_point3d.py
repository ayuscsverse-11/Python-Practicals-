"""Practical 12: Inherit Point2D to create Point3D."""

import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    # Override distance() to include the z coordinate
    def distance(self, other):
        return math.sqrt(
            (self.x - other.x)**2 +
            (self.y - other.y)**2 +
            (self.z - other.z)**2
        )


p1 = Point3D(1, 2, 3)
p2 = Point3D(4, 6, 3)
print("3D distance:", p1.distance(p2))
