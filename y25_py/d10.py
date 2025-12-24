from itertools import product
from z3 import *

def bfs_a(M, B):
    initial_state = tuple(False for _ in range(len(M)))
    Q = [(initial_state, i, 1) for i in range(len(B))]
    V = {(initial_state, i) for i in range(len(B))}
    while Q:
        S, i, n = Q.pop(0)

        S = tuple(not s if idx in B[i] else s for idx, s in enumerate(S))

        if S == M:
            return n

        for i in range(len(B)):
            if (S, i) in V:
                continue
            Q.append((S, i, n+1))
            V.add((S, i))

    return 0


def partA(inp: str):
    C = 0
    for line in inp.split('\n'):
        line = line.split()
        M, B = line[0], line[1:-1]
        M = tuple(False if c == '.' else True for c in M[1:-1])
        B = tuple(tuple(map(int, b[1:-1].split(','))) for b in B)
        r = bfs_a(M, B)
        C += r
    return C

def partB(inp: str):
    C = 0
    lines = inp.split('\n')
    for n, line in enumerate(lines):
        line = line.split()
        B, J = line[1:-1], line[-1]
        J = list(map(int, J[1:-1].split(',')))
        B = [set(map(int, b[1:-1].split(','))) for b in B]

        coeffs = [Int(f'x{i+1}') for i in range(len(B))]
        opt = Optimize()
        for i, j in enumerate(J):
            constraint = sum(c for c, b in zip(coeffs, B) if i in b) == j
            opt.add(constraint)

        for c in coeffs:
            opt.add(c >= 0)

        opt.minimize(sum(coeffs))
        opt.check()
        M = opt.model()
        C += sum(M[c].as_long() for c in coeffs)

    return C

if __name__ == '__main__':
    import sys
    # init_printing(use_unicode=True)

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd10.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
