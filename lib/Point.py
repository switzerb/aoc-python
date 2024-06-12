class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%s,%s)" % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    # manhattan distance = abs(x1 - x2) + abs(y1 - y2)
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
