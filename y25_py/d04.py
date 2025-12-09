from itertools import product

def partA(inp: str):
    S = {(r, c) for r, l in enumerate(inp.splitlines()) for c, ch in enumerate(l) if ch == '@'}
    return len(get_accessible(S))


def partB(inp: str):
    S = {(r, c) for r, l in enumerate(inp.splitlines()) for c, ch in enumerate(l) if ch == '@'}
    C = 0
    while True:
        if not (P := get_accessible(S)): break
        C += len(P)
        S -= P
    return C

def get_accessible(S: set[tuple[int, int]]):
    P = set()
    for (r, c) in S:
        ct = 0
        for (rd, cd) in product((-1, 0, 1), repeat=2):
            ct += (r+rd, c+cd) in S and (rd != 0 or cd != 0)

        if ct >= 4: continue
        P.add((r, c))
    return P

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd04.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
