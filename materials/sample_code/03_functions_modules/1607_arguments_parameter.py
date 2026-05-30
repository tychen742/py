
class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    def getX (self):
        return self.x
    def getY (self):
        return self.y
    def distanceFromOrigin(self):
        return (self.x**2 + self.y**2)** .5

def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = (xdiff**2 + ydiff**2)** .5
    return dist

p = Point(1, 1)
# print(p.distanceFromOrigin())
q = Point(5, 4)
print(distance(p, q))