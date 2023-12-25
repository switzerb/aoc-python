# --- Day 12: Hot Springs ---
# https://adventofcode.com/2023/day/12

import time
from functools import cache


# dynamic programming function parameters are your key so you don't run the function you can just look it up

@cache
def part_one(conditions, groups) -> int:
    if len(groups) == 0:
        return '#' not in conditions
    curr, groups = groups[0], groups[1:]
    remaining = sum(groups)
    res = 0
    for idx in range(len(conditions) - remaining - curr + 1):
        if "#" in conditions[:idx]:
            break
        nxt = idx + curr
        if nxt <= len(conditions) and '.' not in conditions[idx:nxt] and conditions[nxt:nxt + 1] != '#':
            res += part_one(conditions[nxt + 1:], groups)
    return res


def part_two(data):
    return 0


def main():
    filename = open("input.txt")
    data = filename.read().splitlines()
    sums = []
    for each in data:
        conditions, groups_raw = each.split(" ")
        groups = tuple([int(x) for x in groups_raw.split(",")])
        something = part_one(conditions.strip(), groups)
        sums.append(something)
    print(sum(sums))
    # print(part_two(data))


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
