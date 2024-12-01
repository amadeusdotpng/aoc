from collections import Counter

def partA(inp: str):
    L, R = zip(*(map(int, line.split()) for line in inp.splitlines()))
    N = zip(sorted(L), sorted(R))
    return sum(map(lambda n: abs(n[0] - n[1]), N))


def partB(inp: str):
    L, R = zip(*(map(int, line.split()) for line in inp.splitlines()))
    C = Counter(R)
    return sum(n * C[n] for n in L)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd01.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
