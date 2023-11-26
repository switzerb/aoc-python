# https://adventofcode.com/2016/day/7
# --- Day 7: Internet Protocol Version 7 ---
import time
from os import path
import re

SCRIPT_DIR = path.dirname(__file__)
INPUT_FILE = "input.txt"


def parse(data):
    return data


abba_match = re.compile(r"(.)(.)\2\1")
ip_match = re.compile(r"(\w+)(?:\[\w*])*")
hypernet_match = re.compile(r"\[(\w+)\]+")


def contains_abba(seq: str) -> bool:
    """ Check for whether this string contains an ABBA sequence
    ABBA is an Autonomous Bridge Bypass Annotation, or any
    four-character sequence which consists of a pair of two different characters
    followed by the reverse of that pair, such as xyyx or abba.
    e.g. abba is valid. poop is valid. abab is not. """

    matches = abba_match.findall(seq)
    if len(matches) == 0: return False

    a, b = matches[0]
    if a == b: return False
    return True


def supports_tls(ip: str) -> bool:
    hypernets = hypernet_match.findall(ip)
    ips = ip_match.findall(ip)
    # check the square brackets first, if there are any return false
    for h in hypernets:
        if contains_abba(h):
            return False
    for address in ips:
        if contains_abba(address):
            return True
    return False


def part_one(ips: list[str]) -> int:
    """counts the number of valid IP that support TLS"""
    count = 0
    for ip in ips:
        if supports_tls(ip): count += 1
    return count


def main():
    file = path.join(SCRIPT_DIR, INPUT_FILE)
    with open(file, mode="rt") as f:
        data = f.read().splitlines()
    ips = parse(data)
    print("part one: ", part_one(ips))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
