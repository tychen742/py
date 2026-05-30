class Point :
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    def getX (self):
        return self.x
    def getY (self):
        return self.y
    def distanceFromOrgin (self):
        return (self.x**2 + self.y**2) ** .5
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

p = Point(3, 4)
q = Point(4, 3)
print(p.distanceFromOrgin())
print(p.distanceFromOrgin())

print(p)
print(str(q))
