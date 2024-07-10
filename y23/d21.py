from typing import Set, Tuple
from functools import cache
import os

type Position = Tuple[int, int]

def partA(inp: str):
    inp = inp.splitlines()
    HT, WD = len(inp), len(inp[0])

    rocks = set()
    reach = set()
    for row, line in enumerate(inp):
        for col, char in enumerate(line):
            if char == 'S':
                reach.add((row, col));
                continue

            if char == '#':
                rocks.add((row, col))
                continue

    get_edges = lambda row, col: (
            (row-1, col),
            (row+1, col),
            (row, col-1),
            (row, col+1),
    )

    for _ in range(64):
        edges = set([
            (e_row, e_col)
            for row, col in reach
            for e_row, e_col in get_edges(row, col)

            if ((e_row, e_col) not in rocks
            and -1 < e_row < HT
            and -1 < e_col < WD)
        ])
        reach = edges

    return len(reach)


def partB(inp: str):
    pass

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd21.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
