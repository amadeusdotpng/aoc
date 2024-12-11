from math import log10, floor
from functools import cache

def process_stone(stone, limit):
    @cache
    def f(i, stone):
        if i == limit:
            return 1

        if stone == 0:
            res = f(i+1, 1)
            return res

        digits = floor(log10(stone)+1)
        if digits % 2 == 0:
            l_stone = int(stone // (10**(digits/2)))
            r_stone = int(stone % (10**(digits/2)))
            return f(i+1, l_stone) + f(i+1, r_stone)

        return f(i+1, 2024*stone)
    return f(0, stone)

def partA(inp: str):
    stones = list(map(int, inp.split()))
    return sum(process_stone(stone, 25) for stone in stones)

def partB(inp: str):
    stones = list(map(int, inp.split()))
    return sum(process_stone(stone, 75) for stone in stones)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd11.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
