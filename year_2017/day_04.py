import sys
from collections import Counter

from utils import lines


def is_unique(items):
    return len(set(items)) == len(items)


def part1():
    print(sum(map(is_unique, [line.split() for line in lines()])))


def part2():
    x = lines()
    bad = 0
    total = len(x)
    for line in x:
        seen = []
        for word in line.split():
            c = Counter(word)
            if c in seen:
                bad += 1
                break
            seen += [c]
    print(total - bad)


def main():
    part1()


if __name__ == "__main__":
    sys.exit(main())
