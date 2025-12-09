from itertools import combinations, pairwise

def partA(inp: str):
    V = [tuple(map(int, line.split(','))) for line in inp.split('\n')]
    return sorted((abs(ax - bx) + 1) * (abs(by - ay) + 1) for (ax, ay), (bx, by) in combinations(V, 2))[-1]

def partB(inp: str):
    def inside(v):
        x, y = v
        if any(l <= x <= r and y == hy for l, r, hy in E['H']):
            return True

        if any(l <= y <= r and x == vx for l, r, vx in E['V']):
            return True

        y += 1

        p = 0
        while y < V_max:
            p += any(l <= x <= r and y == hy for l, r, hy in E['H'])
            y += 1

        return p % 2 == 1

    V = [tuple(map(int, line.split(','))) for line in inp.split('\n')]
    # H_max = max(V, key=lambda v: v[0])[0]
    V_max = max(V, key=lambda v: v[1])[1]

    E = {'H': set(), 'V': set()}
    for (ax, ay), (bx, by) in pairwise(V):
        if ay == by:
            E['H'].add((*sorted((ax, bx)), by))
            continue
        if ax == bx:
            E['V'].add((*sorted((ay, by)), bx))
            continue

        raise ValueError((ax, ay, bx, by))

    A = 0
    for (ax, ay), (bx, by) in combinations(V, 2):
        v_0 = (ax, by)
        v_1 = (bx, ay)
        if inside(v_0) and inside(v_1):
            print((ax, ay), (bx, by))
            A = max(A, (abs(ax - bx) + 1) * (abs(by - ay) + 1))

    return A

def partB2(inp: str):
    def inside(v):
        x, y = v
        if (x, y) in E:
            return True

        y += 1
        p = 0
        while y < V_max:
            p += (x, y) in E 
            y += 1

        return p % 2 == 1

    V = [tuple(map(int, line.split(','))) for line in inp.split('\n')]
    # H_max = max(V, key=lambda v: v[0])[0]
    V_max = max(V, key=lambda v: v[1])[1]

    E = set()
    for (ax, ay), (bx, by) in pairwise([*V, V[0]]):
        if ay == by:
            E.update((x, by) for x in range(min(ax, bx), max(ax, bx) + 1))
            continue

        if ax == bx:
            E.update((bx, y) for y in range(min(ay, by), max(ay, by) + 1))
            continue

        raise ValueError((ax, ay, bx, by))

    print(len(E))

    A = 0
    c = 0
    for idx, ((ax, ay), (bx, by)) in enumerate(combinations(V, 2)):
        v_0 = (ax, by)
        v_1 = (bx, ay)
        if inside(v_0) and inside(v_1):
            A = max(A, (abs(ax - bx) + 1) * (abs(by - ay) + 1))
            if c % 100 == 0:
                print(f'{idx: >6}/122760 {(ax, ay)}, {(bx, by)}, {A}')
            c += 1

    return A

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd09.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    # print(f'B: {partB(inp[::])}')
    print(f'B: {partB2(inp[::])}')
