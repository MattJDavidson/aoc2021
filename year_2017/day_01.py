import sys

from utils import line_as_int


def part1():
    numbers = list(line_as_int())
    numbers += [numbers[0]]
    print(sum(x for x, y in zip(numbers, numbers[1:]) if x == y))


def part2():
    numbers = list(line_as_int())
    jump = len(numbers) // 2
    numbers2 = numbers[jump:] + numbers[:jump]
    print(sum(x for x, y in zip(numbers, numbers2) if x == y))


def main():
    part2()


if __name__ == "__main__":
    sys.exit(main())
