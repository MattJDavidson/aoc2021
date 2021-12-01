from typing import List

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
