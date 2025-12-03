def partA(inp: str):
    return solve(inp.splitlines(), 2)

def partB(inp: str):
    return solve(inp.splitlines(), 12)

def solve(B, N: int):
    C = 0
    for b in B:
        b = [int(bt) for bt in b]
        t = 0
        for k in range(N-1, -1, -1):
            k_max = max(b) if k == 0 else max(b[:-k]) 
            k_idx = b.index(k_max)
            t = 10 * t + k_max
            b = b[k_idx+1:]
        C += int(t)
    return C


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd03.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
