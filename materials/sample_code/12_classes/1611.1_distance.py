##### distance from origin
##### distance from point
class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def distanceFromOrgin(self):
        return (self.x**2 + self.y**2)**.5

    def distance (self, q):
        return ((self.x - q.x)**2 + (self.y - q.y)**2)**.5


p = Point(0, 0)
q = Point(3, 4)
print(q.distanceFromOrgin())
print(p.distance(q))