from functools import total_ordering
from math import sqrt


@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented


p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(0, 0)

print(f"{abs(p1)} == {abs(p2)}: {p1 == p2}")
print(p1 != p2)
print(p1 < p3)
print(p1 > p3)
print(p1 >= p2)
print(p1 <= p2)
