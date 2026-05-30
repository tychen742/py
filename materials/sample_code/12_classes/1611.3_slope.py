class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def slope_from_origin(self):
        return (self.y - 0) / (self.x - 0)


p = Point(2, 4)
print(p.slope_from_origin())