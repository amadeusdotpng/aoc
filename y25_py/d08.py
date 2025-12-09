from itertools import combinations
from functools import reduce
from math import prod

def partA(inp: str):
    B = [tuple(map(int, line.split(','))) for line in inp.split('\n')]
    D = sorted([(
            (ax, ay, az),
            (bx, by, bz),
            (ax-bx)**2 + (ay-by)**2 + (az-bz)**2
        ) for ((ax, ay, az), (bx, by, bz)) in combinations(B, 2)
    ], key=lambda v: v[2])[:1000]

    C = []
    for (d_0, d_1, _) in D:
        connects = []
        for i in range(len(C)):
            if not(d_0 in C[i] or d_1 in C[i]):
                continue
            connects.append(C[i])

        if not connects:
            C.append({d_0, d_1})
            continue

        for c in connects:
            C.remove(c)

        c = reduce(lambda a, b: a | b, connects)
        c.add(d_0)
        c.add(d_1)
        C.append(c)

    # print('\n'.join(str(e) for e in sorted(C, key=lambda s: len(s))))
    return prod(len(s) for s in list(reversed(sorted(C, key=lambda s: len(s))))[:3])
    

def partB(inp: str):
    B = [tuple(map(int, line.split(','))) for line in inp.split('\n')]
    D = sorted([(
            (ax, ay, az),
            (bx, by, bz),
            (ax-bx)**2 + (ay-by)**2 + (az-bz)**2
        ) for ((ax, ay, az), (bx, by, bz)) in combinations(B, 2)
    ], key=lambda v: v[2])

    C = []
    for (d_0, d_1, _) in D:
        connects = []
        for i in range(len(C)):
            if not(d_0 in C[i] or d_1 in C[i]):
                continue
            connects.append(C[i])

        if not connects:
            C.append({d_0, d_1})
            continue

        for c in connects:
            C.remove(c)

        c = reduce(lambda a, b: a | b, connects)
        c.add(d_0)
        c.add(d_1)
        C.append(c)

        if len(C) == 1 and len(C[0]) == 1000:
            return d_0[0] * d_1[0]
    
if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd08.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
