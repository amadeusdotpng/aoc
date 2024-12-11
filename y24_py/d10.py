from collections import deque


def bfsA(root, map):
    Q = deque([root])
    X = set()

    W, H = len(map)-1, len(map[0])-1

    in_bounds = lambda p: 0 <= p.real <= H and 0 <= p.imag <= W
    get_edges = lambda p: [x for x in [p-1, p+1j, p+1, p-1j] if in_bounds(x) ]

    score = 0

    while Q:
        N = Q.popleft()
        
        height_N = map[int(N.real)][int(N.imag)]
        if height_N == 9:
            score += 1
            continue

        for E in get_edges(N):

            if E in X:
                continue

            height_E = map[int(E.real)][int(E.imag)]
            if height_E-height_N != 1:
                continue

            Q.append(E)
            X.add(E)
    
    return score

def partA(inp: str):
    map = [[int(c) for c in line] for line in inp.splitlines()]
    # print('\n'.join(str(line) for line in map))
    trailheads = []
    for r, line in enumerate(map):
        for c, n in enumerate(line):
            # print(complex(r, c), n)
            if n == 0:
                trailheads.append(complex(r, c))

    S = 0
    for head in trailheads:
        s = bfsA(head, map)
        S += s

    return S

def bfsB(root, map):
    Q = deque([root])
    # X = set()

    W, H = len(map)-1, len(map[0])-1

    in_bounds = lambda p: 0 <= p.real <= H and 0 <= p.imag <= W
    get_edges = lambda p: [x for x in [p-1, p+1j, p+1, p-1j] if in_bounds(x) ]

    rating = 0

    while Q:
        N = Q.popleft()
        
        height_N = map[int(N.real)][int(N.imag)]
        if height_N == 9:
            rating += 1
            continue

        for E in get_edges(N):

            '''
            if E in X:
                continue
            '''

            height_E = map[int(E.real)][int(E.imag)]
            if height_E-height_N != 1:
                continue

            Q.append(E)
            # X.add(E)
    
    return rating

def partB(inp: str):
    map = [[int(c) for c in line] for line in inp.splitlines()]
    # print('\n'.join(str(line) for line in map))
    trailheads = []
    for r, line in enumerate(map):
        for c, n in enumerate(line):
            # print(complex(r, c), n)
            if n == 0:
                trailheads.append(complex(r, c))

    S = 0
    for head in trailheads:
        s = bfsB(head, map)
        S += s

    return S

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd10.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
