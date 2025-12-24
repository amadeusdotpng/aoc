from itertools import combinations, pairwise
from collections import defaultdict
import multiprocessing as mp
from functools import partial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mc
import matplotlib.animation as animation


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

def f(E, p) -> tuple[int, tuple[tuple[int, ...], tuple[int, ...]]]:
    (ax, ay), (bx, by) = p

    min_x, max_x = min(ax, bx), max(ax, bx)
    min_y, max_y = min(ay, by), max(ay, by)
    e_v = [(ax, min_y, max_y), (bx, min_y, max_y)]
    e_h = [(ay, min_x, max_x), (by, min_x, max_x)]
    if any(any(is_intersecting(e, (vx, *vy)) for vy in vys) for e in e_h for vx, vys in E['V'].items()):
        return (0, p)

    if any(any(is_intersecting(e, (hy, *hx)) for hx in hxs) for e in e_v for hy, hxs in E['H'].items()):
        return (0, p)

    s = 1 if ay > by else -1
    if not (is_inside((ax, by+s), E) and is_inside((bx, ay-s), E)):
        return (0, p)


    return ((abs(bx - ax) + 1) * (abs(by - ay) + 1), p)

def partB(inp: str, anim=False):
    P = [tuple(map(int, line.split(','))) for line in inp.split('\n')]
    E = {'H': defaultdict(set), 'V': defaultdict(set)}
    for (ax, ay), (bx, by) in pairwise([*P, P[0]]):
        if ax == bx: E['V'][ax].add((min(ay, by), max(ay, by)))
        if ay == by: E['H'][ay].add((min(ax, bx), max(ax, bx)))

    M = 0
    P1, P2 = None, None
    def frames():
        nonlocal M
        nonlocal P1, P2
        pool = mp.Pool(processes=10)
        for m, (a, b) in pool.imap_unordered(partial(f, E), combinations(P, 2)):
            if m > M:
                M = m
                P1, P2 = a, b

            yield ((a, b), (P1, P2))

    if anim:
        L = [[(ax, ay), (bx, by)] for (ax, ay), (bx, by) in pairwise([*P, P[0]])]
        poly = mc.LineCollection(L)
        rect = mc.LineCollection([], colors=[(1, 0, 0, 1)]*4+[(0, 1, 0, 1)]*4)
        fig, ax = plt.subplots()
        ax.add_collection(poly)
        ax.add_collection(rect)
        ax.autoscale()

        def animate(frame):
            segments = [
                ([(a[0], a[1]), (b[0], a[1])],
                 [(a[0], a[1]), (a[0], b[1])],
                 [(b[0], b[1]), (b[0], a[1])],
                 [(b[0], b[1]), (a[0], b[1])])
                for (a, b) in frame
                if a is not None and b is not None
            ]
            segments = [e for t in segments for e in t]
            rect.set_segments(segments)
            return rect,

        _ = animation.FuncAnimation(fig, animate, frames=frames, interval=30)
        plt.show()
    else:
        for _ in frames(): pass

    return M



if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd09.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
