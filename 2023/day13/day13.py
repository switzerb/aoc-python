# --- Day 13: Point of Incidence ---
# https://adventofcode.com/2023/day/13
import time


def part_one(rows):
    # count of columns to the left of any reflection
    def vertical(block: list[str]) -> int:
        width = len(block[0])
        if width < 2:
            return 0
        for idx in range(width - 1):
            col = [row[idx] for row in block]
            nxt = [row[idx + 1] for row in block]
            if col == nxt:
                flag = True
                left = idx
                right = idx + 1
                while right < width:
                    col = [row[left] for row in block]
                    nxt = [row[right] for row in block]
                    if col == nxt:
                        left -= 1
                        right += 1
                    else:
                        return 0
                if flag:
                    return width - idx
        return 0

    # return index of horizontal reflection
    def horizontal(block):
        height = len(block)
        if height < 2:
            return 0
        for idx in range(height - 1):
            row = block[idx]
            nxt = block[idx + 1]
            if row == nxt:
                return height - idx
        return 0

    v, h = [], []
    for block in rows:
        n = vertical(block)
        if n != 0:
            v += [n]
        else:
            h += [horizontal(block)]
    return sum(v) + (sum(h) * 100)


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
