# --- Day:  ---
# https://adventofcode.com/2023/day/3
import time

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# (x, y)
directions = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
pipe_dirs = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}


def parse(data, entry_char):
    map = {}
    width = 0
    height = 0
    entry_pt = (0, 0)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "S":
                entry_pt = (x, y)
            map[(x, y)] = c
            width = x
        height = y
    return map, width + 1, height + 1, entry_pt, entry_char


def part_one(pipe_map):
    pipes, width, height, entry, entry_char = pipe_map
    tube = list()
    tube.append(entry)

    def move(p, d):
        return p[0] + directions[d][0], p[1] + directions[d][1]

    curr = entry
    prev = curr
    steps = 0
    while True:
        pipe = pipes[curr]
        if pipe == "S":
            pipe = entry_char
        opt1 = move(curr, pipe_dirs[pipe][0])
        opt2 = move(curr, pipe_dirs[pipe][1])
        curr = opt2 if prev == opt1 else opt1
        prev = tube[-1]
        tube.append(curr)
        steps += 1
        if curr == entry:
            break
    return steps // 2


def part_two(data):
    return 0


def main():
    filename = open("input.txt")
    data = filename.read().splitlines()
    print(part_one(parse(data, "-")))
    # print(part_two(data))


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
