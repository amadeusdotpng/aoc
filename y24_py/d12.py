from collections import defaultdict, deque


def bfs(root, map):
    Q = deque([root])
    X = set([root])

    H, W = len(map)-1, len(map[0])-1

    in_bounds = lambda p: 0 <= p.real <= H and 0 <= p.imag <= W
    get_edges = lambda p: [p + p_d for p_d in [-1+0j, 0+1j, 1+0j, 0-1j] if in_bounds(p + p_d)]
    while Q:
        N = Q.popleft()
        for E in get_edges(N):
            if E in X:
                continue

            if map[int(E.real)][int(E.imag)] != map[int(root.real)][int(root.imag)]:
                continue

            Q.append(E)
            X.add(E)

    assert all(map[int(E.real)][int(E.imag)] == map[int(root.real)][int(root.imag)] for E in X)
    return X

def partA(inp: str):
    map = inp.splitlines()
    explored = set()
    regions = {}

    for r, line in enumerate(map):
        for c, _ in enumerate(line):
            root = complex(r, c)
            if root in explored:
                continue
            region = bfs(root, map)
            explored |= region
            regions[root] = region


    perimeters = defaultdict(int)
    for root in regions:
        for p in regions[root]:
            for p_d in [-1+0j, 0+1j, 1+0j, 0-1j]:
                if p + p_d not in regions[root]:
                    perimeters[root] += 1

    S = 0
    for root in regions:
        area = len(regions[root])
        # print(root, area, perimeters[root], area * perimeters[root])
        S += area * perimeters[root]

    return S
    

def get_sides(root, regions):
    Q = deque([root])
    X = set([root])

    get_edges = lambda p: [p + p_d for p_d in [-1+0j, 0+1j, 1+0j, 0-1j]]

    sides_flags = defaultdict(int)
    sides = 0
    while Q:
        N = Q.popleft()

        sides_flag = 0
        if N + (-1+0j) not in regions[root]: sides_flag |= 1 << 0
        if N + ( 0+1j) not in regions[root]: sides_flag |= 1 << 1
        if N + ( 1+0j) not in regions[root]: sides_flag |= 1 << 2
        if N + ( 0-1j) not in regions[root]: sides_flag |= 1 << 3

        sides_flags[N] = sides_flag
        counted_sides = sides_flag

        for E in get_edges(N):
            if E not in regions[root]:
                continue

            if sides_flags[E] & 1 << 0: counted_sides &= ~(1 << 0)
            if sides_flags[E] & 1 << 1: counted_sides &= ~(1 << 1)
            if sides_flags[E] & 1 << 2: counted_sides &= ~(1 << 2)
            if sides_flags[E] & 1 << 3: counted_sides &= ~(1 << 3)

            if E in X:
                continue

            Q.append(E)
            X.add(E)
        
        sides += counted_sides.bit_count()
    return sides
            
def partB(inp: str):
    map = inp.splitlines()
    explored = set()
    regions = {}

    for r, line in enumerate(map):
        for c, _ in enumerate(line):
            root = complex(r, c)
            if root in explored:
                continue
            region = bfs(root, map)
            explored |= region
            regions[root] = region


    sides = {}
    for root in regions:
        sides[root] = get_sides(root, regions)

    S = 0
    for root in regions:
        area = len(regions[root])
        S += area * sides[root]

    return S

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd12.in'
    inp = open(infile).read().strip()
    # print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
