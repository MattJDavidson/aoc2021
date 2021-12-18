from collections import Counter
from typing import List, Iterable

from utils import lines, ints_from_string


def part1():
    fish = list(ints_from_string(lines()[0]))
    for _ in range(80):
        new_fish = fish
        for i, fsh in enumerate(fish):
            if fsh == 0:
                new_fish[i] = 6
                new_fish.append(9)
                continue
            new_fish[i] = fsh - 1
        fish = new_fish
    print(len(fish))


class FishSchool:
    def __init__(self, fish: Iterable[int]):
        self.school = Counter(fish)

    def simulate_day(self) -> "FishSchool":
        self.school = Counter({val - 1: self.school[val] for val in self.school})
        if -1 in self.school:
            self.school[6] += self.school[-1]
            self.school[8] = self.school[-1]
            self.school.pop(-1)
        return self

    def simulate_days(self, days) -> "FishSchool":
        for day in range(days):
            self.simulate_day()
        return self

    def count(self) -> int:
        return sum(self.school.values())


def part2():
    print(FishSchool(ints_from_string(lines()[0])).simulate_days(256).count())


def main():
    # part1() #350917
    part2()  # 1592918715629


if __name__ == "__main__":
    main()
