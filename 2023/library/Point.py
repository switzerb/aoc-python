from library.Grid import Direction


class Point:
    def __init__(self, x=0, y=0, facing=Direction.NORTH):
        self.x = x
        self.y = y
        self.facing = facing

    def __str__(self):
        return "Point(%s,%s,%s)" % (self.x, self.y, self.facing)

    def move_right(self, dist = 1):
        if self.facing == Direction.NORTH:
            self.facing = Direction.EAST
            self.x += dist
        elif self.facing == Direction.SOUTH:
            self.facing = Direction.WEST
            self.x -= dist
        elif self.facing == Direction.EAST:
            self.facing = Direction.SOUTH
            self.y -= dist
        elif self.facing == Direction.WEST:
            self.facing = Direction.NORTH
            self.y += dist
        return self

    def move_left(self, dist = 1):
        if self.facing == Direction.NORTH:
            self.facing = Direction.WEST
            self.x -= dist
        elif self.facing == Direction.SOUTH:
            self.facing = Direction.EAST
            self.x += dist
        elif self.facing == Direction.EAST:
            self.facing = Direction.NORTH
            self.y += dist
        elif self.facing == Direction.WEST:
            self.facing = Direction.SOUTH
            self.y -= dist
        return self

# manhattan distance = abs(x1 - x2) + abs(y1 - y2)
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)