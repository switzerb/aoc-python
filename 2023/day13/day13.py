# --- Day 13: Point of Incidence ---
# https://adventofcode.com/2023/day/13
import time


def part_one(data):
    def distance(l: str, r: str) -> int:
        return sum(a != b for a, b in zip(l, r))

    def reflection(block: list[str]) -> int:
        for idx in range(len(block)):
            if idx == 0:  # no reflection on first row
                continue
            if all(l == r for l, r in zip(reversed(block[:idx]), block[idx:])):
                return idx
        return 0

    def score(block: str) -> int:
        rows = block.split("\n")
        if row := reflection(rows):
            return 100 * row

        # we can just reverse the rows to cols with this one weird trick!
        if col := reflection(list(zip(*rows))):
            return col

        raise ValueError("no reflection found!")

    return sum(score(block) for block in data)


def part_two(data):
    return 0


def main():
    filename = open("input.txt")
    data = filename.read().split("\n\n")
    print(part_one(data))
    # print(part_two(data))


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
