from collections import deque
from typing import List, Tuple

# Naive Brute-force solution
def partA(input: str):
    input = [line.split() for line in input.splitlines()]

    trench = set([0 + 0j])
    c: complex = 0 + 0j

    # Dig perimeter.
    for d, n, _ in input:
        n = int(n)
        match d:
            case 'U': d = 1j
            case 'D': d = -1j
            case 'L': d = -1
            case 'R': d = 1

        for _ in range(n):
            c += d
            trench.add(c)

    minX, minY = int(min(trench, key=lambda c: c.real).real), int(min(trench, key=lambda c: c.imag).imag)
    maxX, maxY = int(max(trench, key=lambda c: c.real).real), int(max(trench, key=lambda c: c.imag).imag)

    # Find a point inside of the perimeter.
    P = None
    for row in range(minY, maxY):
        for col in range(minX, maxX):
            p = complex(col, row)

            intersections = 0
            # print(col, row)
            if p in trench:
                continue


            while p.real < maxX:
                p += 1
                if p in trench:
                    intersections += 1


            if intersections % 2 == 1:
                P = complex(col, row)
                break

    # Dig insides of perimeter.
    Q = deque([P])
    while Q:
        N = Q.popleft()
        for E in (N-1j, N+1j, N+1, N-1):
            if E in trench:
                continue

            Q.append(E)
            trench.add(E)

    # Length of the set should be the area.
    return len(trench)

# Shoelace Theorem + Pick's Theorem + some funky shit to apply it to a block grid
def partB(input: str):
    input: List[str]  = [line.split()[2][2:-1] for line in input.splitlines()]
    input: List[Tuple[int, int]] = [(int(line[:5], 16), [1, -1j, -1, 1j][int(line[-1])]) for line in input]
    
    p: complex = 0 + 0j
    vertices = [p]
    for n, d in input:
        p += d * n
        vertices.append(p)

    A = 0
    for i in range(len(vertices)):
        a = vertices[i]
        b = vertices[(i + 1) % len(vertices)]
        A += 0.5 * ((a.imag + 0) + (b.imag + 0)) * ((a.real + 0) - (b.real + 0))

    A = abs(A)
    for i in range(len(vertices)):
        a = vertices[i]
        b = vertices[(i + 1) % len(vertices)]
        A += 0.5 * abs(a - b)

    return int(A+1)


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd18.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
