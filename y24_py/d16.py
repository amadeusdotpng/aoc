from functools import cache
from heapq import heappush, heappop

@cache
def solve_maze(root, goal, barriers):
    Q = [(0, (*root, 0, {root}))]
    X = {(root, 0): 0}
    
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    get_edges = lambda r, c: [
        (r+D[d][0], c+D[d][1], d) for d in range(4)
        if (r+D[d][0], c+D[d][1]) not in barriers
    ]
    best_cost = float('inf')
    best_tiles = set()

    heappush(Q, (0, (*root, 0, {root})))
    while Q:
        cost_n, (nr, nc, nd, path_n) = heappop(Q)

        if (nr, nc) == goal:
            if cost_n < best_cost:
                best_tiles = path_n
                best_cost = cost_n

            if cost_n == best_cost:
                best_tiles |= path_n


        for er, ec, ed in get_edges(nr, nc):
            cost_e = cost_n + 1
            if ed != nd:
                cost_e += 1000

            if cost_e <= X.get((er, ec, ed), float('inf')):
                heappush(Q, (cost_e, (er, ec, ed, path_n | {(er, ec)})))
                X[(er, ec, ed)] = cost_e

    return best_cost, best_tiles

        
@cache
def parse_input(inp: str):
    M = inp.splitlines()

    S = None
    E = None
    B = set()

    for r, line in enumerate(M):
        for c, char in enumerate(line):
            if char == 'S':
                S = (r, c)
                continue
            if char == 'E':
                E = (r, c)
                continue
            if char == '#':
                B.add((r, c))
                continue

    assert S is not None
    assert E is not None

    return S, E, B


def partA(inp: str):
    S, E, B = parse_input(inp)
    COST, _ = solve_maze(S, E, frozenset(B))
    return COST

def partB(inp: str):
    S, E, B = parse_input(inp)
    _, TILES = solve_maze(S, E, frozenset(B))
    return len(TILES)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd16.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
