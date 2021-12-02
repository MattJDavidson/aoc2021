from itertools import *
import math
import sys

from utils import *

def spiral():
    # taken from pytudes
    x=y=side_length=0
    yield(x,y)
    while True:
        for(dx, dy) in (RIGHT,UP,LEFT,DOWN):
            if dy:
                side_length+=1
            for _ in range(side_length):
                x+=dx
                y+=dy
                yield(x,y)

def spiralsums():
    "Yield the values of a spiral where each square has the sum of the 8 neighbors."
    value = defaultdict(int)
    for p in spiral():
        value[p] = sum(value[q] for q in neighbors8(p)) or 1
        yield value[p]

def part1():
    puzzle_input = 312051
    print(cityblock_distance(nth(spiral(),puzzle_input-1)))


def part2():
    puzzle_input = 312051
    print(first(x for x in spiralsums() if x > puzzle_input))


def main():
    part2()


if __name__ == "__main__":
    sys.exit(main())
