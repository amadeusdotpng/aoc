from collections import namedtuple
from queue import PriorityQueue 
from typing import List, Tuple


def dijkstra(map: List, root: Tuple):
    Q = PriorityQueue()
    Q.put(root)
    visited = set([(root[1], root[2])])

    while Q:
        N = Q.get()
        visited.add((N[1], N[2]))

        for edge in getEdges(N):
            if not (0 <= edge[0] <= len(map)-1) or not (0 <= edge[1] <= len(map[0])-1):
                continue
            if (edge[1], edge[2]) not in visited and edge not in Q:
                continue
            if
            Q.put(edge)


def partA(input: str):
    map = input.splitlines()
    # (priority, row, col, # of steps from last turn, parent)
    root = (0, 0, 0, 0)
    return dijkstra(map, root)


def partB(input: str):
    pass

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd17.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
