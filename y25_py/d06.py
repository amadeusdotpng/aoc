from functools import reduce

def partA(inp: str):
    C = 0

    M = [line.split() for line in inp.split('\n')]
    N, O = M[:-1], M[-1]
    N = [list(map(int, row)) for row in zip(*N)]
    
    for ns, o in zip(N, O):
        if o == '+': C += sum(ns)
        if o == '*': C += reduce(lambda a, b: a*b, ns)

    return C

def partB(inp: str):
    C = 0

    M = [line.split() for line in inp.split('\n')]
    W = len(M[0])

    N, O = M[:-1], M[-1]
    N =  list(zip(*N))

    L = {}
    for idx, ns in enumerate(N):
        l = len(max(ns, key=lambda x: len(x)))
        L[idx] = l

    N = []
    for line in inp.split('\n')[:-1]:
        r = []
        for c in range(W):
            n = line[:L[c]]
            line = line[L[c]+1:]
            r.append(n)
        N.append(r)
    N =  list(zip(*N))

    for c, (ns, o) in enumerate(zip(N, O)):
        ns = list(map(lambda s: int(''.join(s)), zip(*ns)))
        if o == '+': C += sum(ns)
        if o == '*': C += reduce(lambda a, b: a*b, ns)

    return C

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd06.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
