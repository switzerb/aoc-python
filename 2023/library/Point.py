from library.Grid import Direction


class Point:
    def __init__(self, x=0, y=0, facing=Direction.NORTH):
        self.x = x
        self.y = y
        self.facing = facing

    def __str__(self):
        return "Point(%s,%s,%s)" % (self.x, self.y, self.facing)

    def get(self):
        return self
