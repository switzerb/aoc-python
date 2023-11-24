from library.Grid import Direction
from library.Point import Point
from copy import copy

origin = Point(0,0, Direction.NORTH)
def part_one(input):
    current = copy(origin)
    for ins in input:
        dir = ins[0]
        dist = int(ins[1])
        if dir == "R":
            current = current.move_right(dist)
        elif dir == "L":
            current = current.move_left(dist)
    return current.manhattan_distance(origin)


part_one(["R2", "L3"])
