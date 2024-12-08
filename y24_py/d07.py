from functools import cache
from math import log10, floor


@cache
def verifyA(R, V):
    if len(V) == 1:
        return R == V[0]
    return (
           (verifyA(R - V[-1], V[:-1]))
        or (verifyA(R / V[-1], V[:-1]) if R % V[-1] == 0 else False)
    )

def partA(inp: str):
    S = 0
    for line in inp.splitlines():
        R, rest = line.split(': ')
        R = int(R)
        V = tuple(map(int, rest.split()))

        S += R if verifyA(R, V) else 0
    return S
            
@cache
def verifyB(R, V):
    if len(V) == 1:
        return R == V[0]
    return (
           (verifyB(R - V[-1], V[:-1]))
        or (verifyB(R / V[-1], V[:-1]) if R % V[-1] == 0 else False)
        or (verifyB(R//L, V[:-1]) if V[-1] == R % (L := 10**floor(log10(V[-1])+1)) else False)
    )

def partB(inp: str):
    S = 0
    for line in inp.splitlines():
        R, rest = line.split(': ')
        R = int(R)
        V = tuple(map(int, rest.split()))

        S += R if verifyB(R, V) else 0
    return S

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd07.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
