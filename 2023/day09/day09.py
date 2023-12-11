# --- Day 9: Mirage Maintenance ---
# https://adventofcode.com/2023/day/9
import time


def parse(data):
    readings = []
    for line in data:
        split = line.split(" ")
    return [int(x) for x in readings]


def find_next(sequence):
    # base case = all zeros
    if sum(sequence) == 0:
        return 0
    deltas = []
    for each in range(len(sequence) - 1):
        deltas.append(sequence[each + 1] - sequence[each])
    return find_next(deltas) + sequence[-1]


def part_one(data):
    return 0


def part_two(data):
    return 0


def main():
    filename = open("input.txt")
    data = filename.read().splitlines()
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
