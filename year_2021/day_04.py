from collections import deque

from utils import first


def get_input():
    f = open("year_2021/inputs/04.txt", "r")
    l = f.readlines()
    puzzle = [int(_) for _ in l[0].strip("\n").split(",")]
    boards = []
    board = []
    for line in l[2:]:
        if line == "\n":
            boards += [board]
            board = []
        else:
            board += [[int(_) for _ in line.strip("\n").split()]]
    return puzzle, boards


def is_winner(drawn, board):
    return any(all(v in drawn for v in row) for row in board) or any(
        all(row[i] in drawn for row in board) for i in range(len(board)))


def yield_winners(puzzle, boards):
    complete = [False] * len(boards)
    drawn = set(puzzle[:4])
    for last_drawn in puzzle[4:]:
        drawn.add(last_drawn)
        for i, board in enumerate(boards):
            if not complete[i] and is_winner(drawn, board):
                complete[i] = True
                yield result(board, drawn, last_drawn)
                if all(complete):
                    return


def result(board, drawn, last_drawn):
    return sum(num for row in board for num in row if num not in drawn) * last_drawn


def part1():  # 4662
    print(first(yield_winners(*get_input())))


def part2():  # 12080
    print(deque(yield_winners(*get_input()), maxlen=1).pop())


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
