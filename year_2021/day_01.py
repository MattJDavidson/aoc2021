from utils import intlines


def part1():
    numbers = intlines()
    print(sum(map(lambda k: k[1] > k[0], zip(numbers, numbers[1:]))))


def part2():
    numbers = intlines()
    windows = list(map(sum, zip(numbers, numbers[1:], numbers[2:])))
    print(sum(map(lambda k: k[1] > k[0], zip(windows, windows[1:]))))


def main():
    part2()


if __name__ == "__main__":
    main()
