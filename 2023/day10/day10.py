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
directions = {"N": (0, -1), "S": (0, 1), "E": (-1, 0), "W": (1, 0)}
pipe_dirs = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE", ".": "", "S": ""}


def parse(data):
    map = {}
    width = 0
    height = 0
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            map[(x, y)] = c
            width = x
        height = y
    return map, width + 1, height + 1


def part_one(pipe_map):
    pipes, width, height = pipe_map
    tube = list()

    def neighbors(curr):
        n = []
        for d in directions.values():
            n.append((curr[0] + d[0], curr[1] + d[1]))
        return n

    start = [i for i in pipes if pipes[i] == "S"][0]
    pipes[start] = "F"  ## the actual starting pipe
    curr = start
    prev = (-1, -1)
    steps = 0
    while True:
        row, col = curr
        pipe = pipes[curr]
        d1, d2 = pipe_dirs[pipe][0], pipe_dirs[pipe][1]
        row_1, col_1 = row + directions[d1][0], col + directions[d1][1]
        row_2, col_2 = row + directions[d2][0], col + directions[d2][1]
        tube.append((row, col))
        (row, col) = (row_2, col_2) if prev == (row_1, col_1) else (row_1, col_1)
        prev = tube[-1]
        steps += 1
        if (row, col) == start:
            break
    return steps // 2


def part_two(data):
    return 0


def main():
    filename = open("input.txt")
    data = filename.read().splitlines()
    print(part_one(parse(data)))
    # print(part_two(data))


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
