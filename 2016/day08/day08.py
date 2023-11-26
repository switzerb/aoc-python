"""
--- Day 8: Two-Factor Authentication ---
https://adventofcode.com/2016/day/8
"""
from typing import List

Screen = List[List[bool]]


def parse(data):
    for each in data:
        print(each)
    return data


def build_screen(w: int, h: int) -> Screen:
    return [[False] * w for _ in range(h)]


def screen_print(s: Screen) -> str:
    if len(s) == 0:
        return ""

    width = len(s[0])
    height = len(s)
    output = ""
    for row in range(height):
        for col in range(width):
            output += "#" if s[row][col] else "."
            if col == width - 1:
                output += "\n"
    return output


def rect(w: int, h: int, screen: Screen) -> Screen:
    for row in range(h):
        for col in range(w):
            screen[row][col] = True
    return screen


def column(screen, idx):
    return [row[idx] for row in screen]


def rotate_col(col: int, by: int, screen: Screen) -> Screen:
    h = len(screen)
    cols = column(screen, col)

    for i in range(h):
        if i == (h - 1):
            screen[0][col] = cols[h - 1]
        else:
            screen[i + by][col] = cols[i]
    return screen


def rotate_row(row: int, by: int, screen: Screen) -> Screen:
    return screen


def part_one(data):
    start = build_screen(50, 6)
    instructions = parse(data)
    # loop through instructions and process
    print(screen_print(start))
    return 0


def part_two(data):
    screen = build_screen(7, 3)
    rect(3, 2)
    print(screen_print(screen))
    return 0


def main():
    f = open("input.txt")
    data = f.read()
    # print("part one: ", part_one(data))
    # print("part two: ", part_two(data))
