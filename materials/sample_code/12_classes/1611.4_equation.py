class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def get_line_to(self, q):
        m = (self.y - q.y)/(self.x - q.x)
        c = self.y - m*self.x
        return (m, c)




print(Point(4, 11).get_line_to(Point(6, 15)))