from collections import namedtuple
from queue import PriorityQueue 
from re import A
from typing import List, Tuple

U = 1
D = 2
L = 3
R = 4

Node = namedtuple("node", ["pos", "steps", "dir"])

def get_neighbors(M: List, N: Node):
    row, col = N.pos
    return (
        Node((row-1, col), N.steps + 1 if N.dir == U or N.dir == 0 else 1, U),
        Node((row+1, col), N.steps + 1 if N.dir == D or N.dir == 0 else 1, D),
        Node((row, col-1), N.steps + 1 if N.dir == L or N.dir == 0 else 1, L),
        Node((row, col+1), N.steps + 1 if N.dir == R or N.dir == 0 else 1, R),
    )

def dijkstra(M: List, root: Node, max_steps: int, min_steps: int | None = None):
    END_POS = (len(M) - 1, len(M[0]) - 1)

    end_cost = None
    visited = set()
    pq: PriorityQueue[Tuple[int, Node]] = PriorityQueue()

    pq.put(root)

    while not pq.empty():
        cost, N = pq.get(block=False)
        if N.pos == END_POS and (min_steps is None or N.steps >= min_steps):
            end_cost = cost
            break

        for E in get_neighbors(M, N):
            if (E.pos, E.steps, E.dir) in visited:
                continue

            if not (0 <= E.pos[0] <= END_POS[0] and 0 <= E.pos[1] <= END_POS[1] ):
                    continue

            if E.steps > max_steps:
                continue

            match (N.dir, E.dir):
                case (1, 2) | (2, 1) | (3, 4) | (4, 3): continue

            if (min_steps is not None
            and N.steps < min_steps
            and N.dir != 0
            and E.dir != N.dir 
            ):
                continue


            row, col = E.pos

            e_cost = cost + M[row][col]

            visited.add((E.pos, E.steps, E.dir))
            pq.put((e_cost, E), block=False)

    return end_cost

def partA(input: str):
    cost_map = [[int(c) for c in line ] for line in input.splitlines()]
    # (cost, row, col, # of steps from last turn, direction)
    root = (0, Node((0, 0), 0, 0))
    return dijkstra(cost_map, root, 3)


def partB(input: str):
    cost_map = [[int(c) for c in line ] for line in input.splitlines()]
    # (cost, row, col, # of steps from last turn, direction)
    root = (0, Node((0, 0), 0, 0))
    return dijkstra(cost_map, root, 10, 4)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd17.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
