# # --- Day:  ---
# # https://adventofcode.com/2023/day/3
# import time
#
#
# def part_one(data):
#     return 0
#
#
# def part_two(data):
#     return 0
#
#

# !/usr/bin/env python3

import sys


def sum_distances(counts, multiplier):
    total = partial_sum = previous = space = 0

    for n in counts:
        if n:
            total += n * (previous * space - partial_sum)
            partial_sum += n * space
            previous += n
            space += 1
        else:
            space += multiplier

    return total


def solve(row_counts, col_counts, multiplier):
    return sum_distances(row_counts, multiplier) + sum_distances(col_counts, multiplier)


# Open the first argument as input or use stdin if no arguments were given
fin = open("input.txt")

grid = list(map(str.rstrip, fin))
row_counts = [0] * len(grid)
col_counts = [0] * len(grid[0])

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == '#':
            row_counts[r] += 1
            col_counts[c] += 1

# def main():
#     filename = open("input.txt")
#     data = filename.read().splitlines()
#     print(part_one(data))
#     print(part_two(data))
#
#
# if __name__ == '__main__':
#     t1 = time.perf_counter()
#     main()
#     t2 = time.perf_counter()
#     print(f"Execution time: {t2 - t1:0.4f} seconds")


total1 = solve(row_counts, col_counts, 2)
print('Part 1:', total1)

total2 = solve(row_counts, col_counts, 1000000)
print('Part 2:', total2)
