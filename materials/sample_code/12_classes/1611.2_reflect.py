class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def reflect_x(self):
        self.y = -(self.y)
        return Point(self.x, self.y)

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

p = Point(3, 5)

print(p)
print(p.reflect_x())
