
from utils import lines


def part1():
    depth = 0
    horizontal = 0
    for line in lines():
        parts = line.split()
        if "forward" in parts[0]:
            horizontal += int(parts[1])
        if "down" in parts[0]:
            depth += int(parts[1])
        if "up" in parts[0]:
            depth -= int(parts[1])
    print(depth*horizontal)


def part2():
    depth = 0
    horizontal = 0
    aim = 0
    x = lines()
    for line in x:
        parts = line.split()
        if "forward" in parts[0]:
            horizontal += int(parts[1])
            depth += aim*int(parts[1])
        if "down" in parts[0]:
            aim += int(parts[1])
        if "up" in parts[0]:
            aim -= int(parts[1])
    print(depth*horizontal)


def main():
    part2()


if __name__ == "__main__":
    main()
