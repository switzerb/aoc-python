# --- Day:  ---
# https://adventofcode.com/2023/day/12
import time


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
