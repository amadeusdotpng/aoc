from typing import Tuple, List
from functools import cache

type Position = Tuple[int, int]

def get_edges(row: int, col: int):
    return  (
        (row-1, col),
        (row+1, col),
        (row, col-1),
        (row, col+1),
    )

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


def row_multiplication(coeff: float, row: List[float]):
    return [coeff*p for p in row]

def row_addition(row0: List[float], row1: List[float]):
    return [p0 + p1 for p0, p1 in zip(row0, row1)]

def gauss_jordan(matrix: List[List[float]]):
    n_rows = len(matrix)
    for i in range(n_rows):
        matrix[i] = row_multiplication(matrix[i][i]**-1, matrix[i])
        for j in range(1,n_rows):
            inverse = row_multiplication(-1 * matrix[(i+j)%n_rows][i], matrix[i])
            matrix[(i+j)%n_rows] = row_addition(matrix[(i+j)%n_rows], inverse)

    return matrix

def partB(inp: str):
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

    points = []
    for step in range(65 + (2 * 131)):
        edges = set([
            (e_row, e_col)
            for row, col in reach
            for e_row, e_col in get_edges(row, col)

            if (e_row % HT, e_col % WD) not in rocks
        ])
        reach = edges

        if step + 1 == 65 or step + 1 == 65 + 131 or step + 1 == 65 + (2 * 131):
            points.append((step + 1, len(reach)))

    matrix = [
        [points[0][0] * points[0][0], points[0][0], 1, points[0][1]],
        [points[1][0] * points[1][0], points[1][0], 1, points[1][1]],
        [points[2][0] * points[2][0], points[2][0], 1, points[2][1]],
    ]

    coeff = gauss_jordan(matrix[::])
    coeff = [coeff[0][-1], coeff[1][-1], coeff[2][-1]]

    x = 26501365
    return int(coeff[0] * x * x + coeff[1] * x + coeff[2])
        


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd21.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
