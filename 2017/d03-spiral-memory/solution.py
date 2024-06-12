import math

from lib.Point import Point

# input = 361527
PORT = Point(0, 0)


# takes a square root and returns a coord on spiral
def get_coord(n: int, depth=0) -> Point:
    if n == 1:
        return Point(0, 0)
    if n == 2:
        return Point(0, 1)
    else:
        if n % 2 == 0:  # even
            pos = get_coord(n - 1, depth + 1)
            return Point(-pos.x, abs(pos.y) + 1)
        else:  # odd
            pos = get_coord(n - 1, depth)
            return Point(abs(pos.x) + 1, -pos.y)


def get_offset(n: int) -> Point:
    # get nearest square root
    root = math.sqrt(n)
    floor = math.floor(root)
    # number is an integer square root
    if root % 1 == 0:
        return get_coord(floor)

    ceil = floor + 1
    offset = (ceil ** 2) - n
    anchor = get_coord(ceil)
    turn = (floor ** 2) + floor
    if ceil % 2 == 0:  # even
        if turn < n:  # closer to ceiling root
            return Point(anchor.x + offset, anchor.y)
        else:  # closer to floor root
            return Point(anchor.x + floor, anchor.y - (offset - floor))
    else:  # odd
        if turn < n:  # closer to ceiling root
            return Point(anchor.x - offset, anchor.y)
        else:  # closer to floor root
            return Point(anchor.x - floor, anchor.y + (offset - floor))


def part_one(input: int):
    offset = get_offset(input)
    print(offset)
    pt = Point(0, 0)
    return pt.manhattan_distance(PORT)
