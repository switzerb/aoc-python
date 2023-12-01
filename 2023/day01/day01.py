import time
import regex


def part_one(inputs):
    total = 0
    for text in inputs:
        d = regex.findall(r'\d', text)
        if len(d) == 0:
            continue
        if len(d) == 1:
            num = d[0] + d[0]
            total += int(num)
        else:
            num = d[0] + d[-1]
            total += int(num)
    return total


def part_two(inputs):
    return 0


def main():
    filename = open("input.txt")
    data = filename.read().splitlines()
    print(part_one(data))
    # print(part_two())


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
