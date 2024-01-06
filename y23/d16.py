from collections import deque
from functools import partial
from itertools import chain
import multiprocessing as mp
from typing import List, Tuple

def getEdges(map: List, N: Tuple):
    match (map[N[0]][N[1]], N[2]):
        case ('-', '^') | ('-', 'v'): # left + right
            return [(N[0], N[1]-1, '<'),(N[0], N[1]+1, '>')]
        case ('|', '>') | ('|', '<'): # up + down
            return [(N[0]-1, N[1], '^'),(N[0]+1, N[1], 'v')]
        case ('.', '^') | ('|', '^') | ('/', '>') | ('\\', '<'): # up
            return [(N[0]-1, N[1], '^')]
        case ('.', '>') | ('-', '>') | ('/', '^') | ('\\', 'v'): # right
            return [(N[0], N[1]+1, '>')]
        case ('.', 'v') | ('|', 'v') | ('/', '<') | ('\\', '>'): # down
            return [(N[0]+1, N[1], 'v')]
        case ('.', '<') | ('-', '<') | ('/', 'v') | ('\\', '^'): # left
            return [(N[0], N[1]-1, '<')]

def bfs(map: List, root: Tuple):
    Q = deque()
    Q.append(root)
    visited = set([root])

    while Q:
        N = Q.pop()
        for edge in getEdges(map, N):
            if not (0 <= edge[0] <= len(map)-1) or not (0 <= edge[1] <= len(map[0])-1):
                continue
            if edge in visited:
                continue
            Q.append(edge)
            visited.add(edge)

    return len(set((N[0], N[1]) for N in visited))

def partA(input: str):
    map = input.splitlines()
    root = (0, 0, '>')
    return bfs(map, root)

def partB(input: str):
    map = input.splitlines()
    roots = chain(
        ((0, i, 'v') for i in range(len(map[0]))),          # Top Edge
        ((j, len(map[0])-1, '<') for j in range(len(map))), # Right Edge
        ((len(map)-1, i, '>') for i in range(len(map[0]))), # Bottom Edge
        ((j, 0, '<') for j in range(len(map)))              # Left Edge
    )

    F = partial(bfs, map)
    pool = mp.Pool(processes=8)

    return max(pool.map(F, roots))

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd16.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
