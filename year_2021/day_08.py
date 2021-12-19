from collections import Counter
from functools import lru_cache
from typing import List, Iterable, Tuple

from utils import lines, ints_from_string


def single_outputs(x):
    y, z = x.split("|")
    y = y.split()
    z = z.split()
    return y, z


def is_1478(string):
    return len(string) in [2, 4, 3, 7]


def digit_combombulator(options: List[str]) -> List[set]:
    one = set([option for option in options if len(option) == 2][0])
    four = set([option for option in options if len(option) == 4][0])
    seven = set([option for option in options if len(option) == 3][0])
    eight = set([option for option in options if len(option) == 7][0])
    candidates_2_3_5 = [
        set(_) for _ in [option for option in options if len(option) == 5]
    ]
    candidates_0_6_9 = [
        set(_) for _ in [option for option in options if len(option) == 6]
    ]

    nine = set()
    for c in candidates_0_6_9:
        if four.issubset(c):
            nine = c
            candidates_0_6_9.remove(c)
            break
    if seven.issubset(candidates_0_6_9[0]):
        zero, six = candidates_0_6_9
    else:
        six, zero = candidates_0_6_9

    three = set()
    for c in candidates_2_3_5:
        if seven.issubset(c):
            three = c
            candidates_2_3_5.remove(c)
            break
    if len(four.intersection(candidates_2_3_5[0])) == 3:
        five, two = candidates_2_3_5
    else:
        two, five = candidates_2_3_5
    return [zero, one, two, three, four, five, six, seven, eight, nine]


def part1():
    linez: Iterable[Tuple[List[str], List[str]]] = map(single_outputs, lines())
    total = 0
    for line in linez:
        i, o = line
        total += sum(map(is_1478, o))
    print(total)


def part2():
    linez: Iterable[Tuple[List[str], List[str]]] = map(single_outputs, lines())
    total = 0
    for line in linez:
        digits, problem = line
        digit_index = digit_combombulator(digits)
        total += int("".join(str(digit_index.index(set(digit))) for digit in problem))

    print(total)


def main():
    # part1()  # 548
    part2()  # 1074888


if __name__ == "__main__":
    main()
