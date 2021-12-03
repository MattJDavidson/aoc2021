from collections import Counter

from utils import lines


def part1():
    x = lines()
    c = [
        Counter(),
        Counter(),
        Counter(),
        Counter(),
        Counter(),
        Counter(),
        Counter(),
        Counter(),
        Counter(),
        Counter(),
        Counter(),
        Counter(),
    ]

    for line in x:
        for i, char in enumerate(line):
            c[i].update(char)
    most = ""
    least = ""
    for _ in c:
        if _["0"] > _["1"]:
            most += "0"
            least += "1"
        else:
            most += "1"
            least += "0"

    print(most, least)
    print(int(most, 2) * int(least, 2))


def part2():
    x = lines()

    possible_ox = list(x)
    possible_co = list(x)
    for i in range(len(x[0])):
        if len(possible_ox) > 1:
            c = Counter([line[i] for line in possible_ox])
            if c["1"] >= c["0"]:
                possible_ox = list(filter(lambda k: k[i] == "1", possible_ox))
            else:
                possible_ox = list(filter(lambda k: k[i] == "0", possible_ox))
        if len(possible_co) > 1:
            c = Counter([line[i] for line in possible_co])
            if c["1"] >= c["0"]:
                possible_co = list(filter(lambda k: k[i] == "0", possible_co))
            else:
                possible_co = list(filter(lambda k: k[i] == "1", possible_co))
    print(int(possible_ox[0], 2) * int(possible_co[0], 2))


def main():
    part2()


if __name__ == "__main__":
    main()
