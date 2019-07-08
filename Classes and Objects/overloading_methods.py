'''This is about making methods already built into python work with your personal class'''

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def distance(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __gt__(self, p):
        return self.distance() > p.distance()

    def __ge__(self, p):
        return self.distance() >= p.distance()

    def __lt__(self, p):
        return self.distance() < p.distance()

    def __le__(self, p):
        return self.distance() <= p.distance()

    def __eq__(self, p):
        return self.distance() == p.distance()

    def __str__(self):
        return f"({str(self.x)}, {str(self.y)})"


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = p1 + p2
p6 = p4 - p1
p7 = p1 * p3

print(p5, p6, p7)
