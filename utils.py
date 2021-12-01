from typing import List, Generator

from pyrival.misc.FastIO import input


def intlines() -> List[int]:
    output = []
    while True:
        y = input()
        if not y:
            break
        output.append(int(y))
    return output


def lines() -> List[str]:
    output = []
    while True:
        y = input()
        if not y:
            break
        output.append(y)
    return output


def line_as_int() -> Generator[int, None, None]:
    return (int(c) for c in (lines()[0]))
