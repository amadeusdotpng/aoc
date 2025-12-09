def partA(inp: str):
    C, R = 0, 50
    for line in inp.splitlines():
        d, r = line[0], int(line[1:])
        C += (R := (R + (1 if d == 'R' else -1) * r) % 100) == 0
    return C



def partB(inp: str):
    C, R = 0, 50
    for line in inp.splitlines():
        d, rs = line[0], int(line[1:])
        r = R + (1 if d == 'R' else -1) * rs
        C += abs(r) // 100 + (1 if r < 0 < R else 0) + (1 if r == 0 else 0) 
        R = r % 100
    return C

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd01.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
