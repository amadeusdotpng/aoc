from collections import defaultdict

def solve(inp: str):
    M = [(p % 2, [c for c in line.strip('.')[::2]]) for p, line in enumerate(inp.splitlines()[2::2])]

    C = 0
    P_0 = defaultdict(int, {(0, 0): 1})
    for (k, (e, ms)) in enumerate(M):
        P_1 = defaultdict(int)
        P = [(i, k-i) for i in range(k+1)]

        for (a, b), m in zip(P, ms):
            if m == '^':
                P_1[(a+1, b)] += P_0[(a, b)]
                P_1[(a, b+1)] += P_0[(a, b)]
                C += P_0[(a, b)] != 0
            if m == '.':
                P_1[(a+1, b+1)] += P_0[(a, b)]
        
        for (a, b), v in P_0.items():
            if (a+b)%2 == e: continue
            P_1[(a, b)] += v

        P_0 = P_1

    return C, sum(P_0.values())

def partA(inp: str):
    return solve(inp)[0]


def partB(inp: str):
    return solve(inp)[1]

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd07.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
