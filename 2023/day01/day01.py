from library.Grid import Direction
from library.Point import Point


# manhattan distance = abs(x1 - x2) + abs(y1 - y2)

def manhattan_distance(p1, p2):
    return abs(p1[0] - p1[1]) + abs(p2[0] - p2[1])


def move(current, turn):
    return 0
def part_one(input):
    current = Point(0,0, Direction.NORTH)
    print(current)
    for i in input:
        dir = i[0]
        dist = i[1]
        print(dir)
        print(dist)
    return 0


part_one(["R2", "L3"])
