from typing import List

from pyrival.misc.FastIO import input

def intlines()-> List[int]:
    lines = []
    while(True):
        y=input()
        if not y:
            break
        lines.append(int(y))
    return lines

def lines()-> List[str]:
    lines = []
    while(True):
        y=input()
        if not y:
            break
        lines.append(y)
    return lines


