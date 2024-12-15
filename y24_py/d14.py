def partA(inp: str):
    inp = inp.splitlines()
    P = {}
    V = {}

    W, H = 101, 103
    for idx, line in enumerate(inp):
        p, v = line.split()
        px, py = map(int, p[2:].split(','))
        vx, vy = map(int, v[2:].split(','))
        P[idx] = (px, py)
        V[idx] = (vx, vy)

    for _ in range(100):
        for idx in P:
            px, py = P[idx]
            vx, vy = V[idx]
            P[idx] = ((px + vx) % W, (py + vy) % H)

    TL = 0
    BL = 0
    TR = 0
    BR = 0
    for idx in P:
        px, py = P[idx]
        if px < W // 2 and py < H // 2:
            TL += 1
            continue
        if px < W // 2 and py > H // 2:
            BL += 1
            continue
        if px > W // 2 and py < H // 2:
            TR += 1
            continue
        if px > W // 2 and py > H // 2:
            BR += 1
            continue

    return TL * BL * TR * BR


def partB(inp: str):
    inp = inp.splitlines()
    P = {}
    V = {}

    W, H = 101, 103
    for idx, line in enumerate(inp):
        p, v = line.split()
        px, py = map(int, p[2:].split(','))
        vx, vy = map(int, v[2:].split(','))
        P[idx] = (px, py)
        V[idx] = (vx, vy)

    s = 0
    while True:
        positions = set(P.values())
        if len(P) ==  len(positions):
            return s
        '''
        if (s - 98) % 101 == 0: 
            M = '\n'.join(''.join('0' if (c, r) in positions else '.' for c in range(W)) for r in range(H))
            print(str(s)+'\n'+M)
            input()
        '''
        for idx in P:
            px, py = P[idx]
            vx, vy = V[idx]
            P[idx] = ((px + vx) % W, (py + vy) % H)
        s += 1


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd14.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
