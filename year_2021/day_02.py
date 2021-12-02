from utils import lines


def part1():
    depth = 0
    horizontal = 0
    for line in lines():
        movement, distance = line.split()
        distance = int(distance)
        if movement == "forward":
            horizontal += distance
        if movement == "down":
            depth += distance
        if movement == "up":
            depth -= distance
    print(depth * horizontal)


def part2():
    depth = 0
    horizontal = 0
    aim = 0
    for line in lines():
        movement, distance = line.split()
        distance = int(distance)
        if movement == "forward":
            horizontal += distance
            depth += aim * distance
        if movement == "down":
            aim += distance
        if movement == "up":
            aim -= distance
    print(depth * horizontal)


def main():
    part2()


if __name__ == "__main__":
    main()
