class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return "x=" + self.x + " , y=" + self.y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return self.x, self.y

p = Point(1, 1)
print(p.move(2, 2))