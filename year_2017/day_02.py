import itertools
import sys

from utils import line_as_int, lines


def part1():
    x = lines()

    vals = []
    for line in x:
        nums = [int(_) for _ in line.split()]
        vals += [max(nums)-min(nums)]

    print(sum(vals))


def part2():
    x = lines()

    vals = []
    for line in x:
        nums = [int(_) for _ in line.split()]
        for x,y in (itertools.combinations(nums,2)):
            if x%y ==0 or y%x ==0:
                res = x//y if x > y else y//x
                vals += [res]
                break

    print(sum(vals))



def main():
    part2()


if __name__ == "__main__":
    sys.exit(main())
