from collections import defaultdict

from utils import lines, ints_from_string, Line


def part1():
    the_lines = (Line.from_ints(*ints_from_string(_)) for _ in lines())
    floor = defaultdict(int)

    for line in the_lines:
        if not line.is_diagonal():
            for point in line.points():
                floor[point] += 1
    print(sum([1 for i in floor if floor[i] > 1]))


def part2():
    the_lines = (Line.from_ints(*ints_from_string(_)) for _ in lines())
    floor = defaultdict(int)

    for line in the_lines:
        for point in line.points(diagonal=True):
            floor[point] += 1
    print(sum([1 for i in floor if floor[i] > 1]))


def main():
    part1() # 7269
    # part2()  # 21140


if __name__ == "__main__":
    main()
