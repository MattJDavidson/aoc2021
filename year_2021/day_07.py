from collections import Counter
from functools import lru_cache
from typing import List, Iterable

from utils import lines, ints_from_string


def part1():
    crabs = list(ints_from_string(lines()[0]))
    fuel = Counter()
    for position in range(min(crabs), max(crabs)):
        for crab in crabs:
            fuel[position] += abs(crab - position)
    print(fuel[min(fuel, key=fuel.get)])

@lru_cache(maxsize=2000, typed=False)
def increasing_amount(goal:int):
    total = 0
    loops = 0
    while loops!=goal:
        loops+=1
        total+=loops
    return total

def part2():
    crabs = list(ints_from_string(lines()[0]))
    fuel = Counter()
    for position in range(min(crabs), max(crabs)):
        print(position)
        for crab in crabs:
            fuel[position] += increasing_amount(abs(crab - position))
    print(fuel[min(fuel, key=fuel.get)])


def main():
    # part1()  # 347449
    part2()  # 98039527


if __name__ == "__main__":
    main()
