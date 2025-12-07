from collections import defaultdict

def partA(inp: str):
    C = 0
    S = defaultdict(set)
    B = defaultdict(set)

    lines = inp.splitlines()
    L = len(lines)
    for r, line in enumerate(lines):
        for c, cr in enumerate(line):
            if cr == 'S': S[r].add(c)
            if cr == '^': B[r].add(c)


    for r in range(L):
        if r not in B: continue
        
        for b in B[r]:
            r_b = r - 1
            while True:
                if r_b < 0: break
                if r_b in B and b in B[r_b]: break

                if r_b in S and b in S[r_b]:
                    S[r].add(b - 1)
                    S[r].add(b + 1)
                    C += 1
                    break

                r_b -= 1

    return C


def partB(inp: str):
    B = defaultdict(set)
    P = defaultdict(set)

    C_0 = defaultdict(int)

    lines = inp.splitlines()
    H = len(lines)
    for r, line in enumerate(lines):
        for c, cr in enumerate(line):
            if cr == 'S':
                B[r].add(c)
                C_0[c] = 1
            if cr == '^': P[r].add(c)

    for r in range(H):
        if r not in P: continue

        C_1 = defaultdict(int)
        for p in P[r]:
            r_p = r - 1
            while True:
                if r_p < 0: break
                if r_p in P and p in P[r_p]: break

                if r_p in B and p in B[r_p]:
                    B[r].add(p - 1)
                    B[r].add(p + 1)
                    C_1[p-1] += C_0[p]
                    C_1[p+1] += C_0[p]
                    break

                r_p -= 1

        for (c_b, c) in C_0.items():
            C_1[c_b] += 0 if c_b in P[r] else c

        C_0 = C_1

    return sum(C_0.values())

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd07.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
