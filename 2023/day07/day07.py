# --- Day 2: Cube Conundrum ---
# https://adventofcode.com/2023/day/3
import time
from collections import Counter

types = []

# Five of a kind, where all five cards have the same label: AAAAA

# Four of a kind, where four cards have the same label and one card has a different label: AA8AA

# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332

# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98

# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432

# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4

# High card, where all cards' labels are distinct: 23456

# rank == index + 1

card_rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def parse(data):
    cards = []
    for hand in data:
        cards.append(tuple(hand.strip().split(" ")))
    return cards


def get_type_rank(card):
    hist = Counter(card)
    counts = hist.most_common()
    if len(counts) == 1: return 7  # "five-of-kind"
    if len(counts) == 5: return 1  # "high-card"
    if counts[0][1] == 4: return 6  # "four-of-kind"
    if counts[0][1] == 3 and counts[1][1] == 2: return 5  # "full-house"
    if counts[0][1] == 3 and counts[1][1] == 1 and counts[2][1] == 1: return 4  # "three-of-kind"
    if counts[0][1] == 2 and counts[1][1] == 2 and counts[2][1] == 1: return 3  # "two-pair"
    if counts[0][1] == 2 and counts[1][1] == 1 and counts[2][1] == 1: return 2  # "one-pair"


def compare(card):
    type_rank = get_type_rank(card[0])
    rank = tuple([card_rank.index(c) for c in card[0]])
    return type_rank, *rank


def part_one(cards):
    winnings = []
    s = sorted(cards, key=compare)
    for idx, each in enumerate(s):
        winnings.append(int(each[1]) * (idx + 1))
    return sum(winnings)


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
