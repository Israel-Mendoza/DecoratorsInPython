def complete_ordering(cls):
    """
    Class decorator that fills in missing ordering methods,
    provided __eq__ and __lt__ are implemented.
    """
    if "__eq__" in dir(cls) and "__lt__" in dir(cls):
        cls.__ne__ = lambda self, other: not self == other
        cls.__gt__ = lambda self, other: not self < other
        cls.__ge__ = lambda self, other: self == other or self > other
        cls.__le__ = lambda self, other: self == other or self < other
    else:
        raise AttributeError("Either __eq__ or __lt__ are not implemented.")
    return cls


class Point:
    """A class to represent a two-dimension point"""

    from math import sqrt

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


Point = complete_ordering(Point)

p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(0, 0)

print(p1 == p2)
print(p1 != p2)
print(p1 < p3)
print(p1 > p3)
print(p1 >= p2)
print(p1 <= p2)
print(dir(Point))
