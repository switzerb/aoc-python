# --- Day 8: Haunted Wasteland ---
# https://adventofcode.com/2023/day/8
import time

START = "AAA"
END = "ZZZ"

GET = {
    "L": 0,
    "R": 1
}


def parse(data):
    turns = data[0].strip()
    map = {}
    for line in data[2:]:
        info = line.split("=")
        n = tuple(info[1].strip().split(","))
        nodes = n[0][1:].strip(), n[1][:-1].strip()
        map[info[0].strip()] = nodes
    return turns, map


def next_turn(iterable):
    while True:
        yield from iterable


def part_one(data):
    turns, desert = data
    temp = next_turn(turns)
    steps = 0
    node = START

    while node != END:
        turn = next(temp)
        node = desert[node][GET[turn]]
        steps += 1

    return steps


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
