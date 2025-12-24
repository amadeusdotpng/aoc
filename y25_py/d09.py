from itertools import combinations, pairwise
from collections import defaultdict
import multiprocessing as mp
from functools import partial


def partA(inp: str):
    P = [tuple(map(int, line.split(','))) for line in inp.split('\n')]
    return sorted((abs(bx - ax) + 1) * (abs(by - ay) + 1) for (ax, ay), (bx, by) in combinations(P, 2))[-1]

def is_intersecting(e_1, e_2):
    return e_2[1] < e_1[0] < e_2[2] and e_1[1] < e_2[0] < e_1[2]

def is_inside(p, E):
    px, py = p
    intersections = 0
    inside_horizontal = False
    while px > 0:
        if any(b <= py <= t for b, t in E['V'][px]) and not inside_horizontal:
            intersections += 1

        inside_horizontal = any(l <= px <= r for l, r in E['H'][py])
        px -= 1

    return intersections % 2 == 1

def f(E, p):
    (ax, ay), (bx, by) = p
    if not (is_inside((ax, by), E) and is_inside((bx, ay), E)):
        return 0

    min_x, max_x = min(ax, bx), max(ax, bx)
    min_y, max_y = min(ay, by), max(ay, by)
    e_v = [(ax, min_y, max_y), (bx, min_y, max_y)]
    e_h = [(ay, min_x, max_x), (by, min_x, max_x)]

    if any(any(is_intersecting(e, (vx, *vy)) for vy in vys) for e in e_h for vx, vys in E['V'].items()):
        return 0

    if any(any(is_intersecting(e, (hy, *hx)) for hx in hxs) for e in e_v for hy, hxs in E['H'].items()):
        return 0

    return (abs(bx - ax) + 1) * (abs(by - ay) + 1)

def partB(inp: str):
    P = [tuple(map(int, line.split(','))) for line in inp.split('\n')]
    E = {'H': defaultdict(set), 'V': defaultdict(set)}
    for (ax, ay), (bx, by) in pairwise([*P, P[0]]):
        if ax == bx: E['V'][ax].add((min(ay, by), max(ay, by)))
        if ay == by: E['H'][ay].add((min(ax, bx), max(ax, bx)))

    pool = mp.Pool(processes=10)
    M = 0
    for n, m in enumerate(pool.imap_unordered(partial(f, E), combinations(P, 2))):
        M = max(M, m)
        if n % 100 == 0:
            print(f'\r{n: >6}/122760')

    # M = 0
    # P1, P2 = None, None
    # for n, ((ax, ay), (bx, by)) in enumerate(combinations(P, 2)):
    #     if n % 100 == 0:
    #         print(f'{n}/120786')
    #     A = (abs(bx - ax) + 1) * (abs(by - ay) + 1)
    #     if not (is_inside((ax, by), E) and is_inside((bx, ay), E)):
    #         if (ax, ay) == (9, 5) and (bx, by) == (2, 3) or (ax, ay) == (2, 3) and (bx, by) == (9, 5):
    #             print('one of the points are outside')
    #             print((ax, by), is_inside((ax, by), E))
    #             print((bx, ay), is_inside((bx, ay), E))

    #         continue

    #     min_x, max_x = min(ax, bx), max(ax, bx)
    #     min_y, max_y = min(ay, by), max(ay, by)
    #     e_v = [(ax, min_y, max_y), (bx, min_y, max_y)]
    #     e_h = [(ay, min_x, max_x), (by, min_x, max_x)]

    #     if any(any(is_intersecting(e, (vx, *vy)) for vy in vys) for e in e_h for vx, vys in E['V'].items()):
    #         if (ax, ay) == (9, 5) and (bx, by) == (2, 3) or (ax, ay) == (2, 3) and (bx, by) == (9, 5):
    #             print('horizontal edge is intersecting vertical edge')
    #         continue

    #     if any(any(is_intersecting(e, (hy, *hx)) for hx in hxs) for e in e_v for hy, hxs in E['H'].items()):
    #         if (ax, ay) == (9, 5) and (bx, by) == (2, 3) or (ax, ay) == (2, 3) and (bx, by) == (9, 5):
    #             print('vertical edge is intersecting horizontal edge')
    #         continue

    #     if A > M:
    #         M = A
    #         P1, P2 = (ax, ay), (bx, by)


    return M



if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd09.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
