from collections import deque

def get_edges(node):
    y, x = node
    return [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]

def bfs():
    root = (0,0)
    Q = deque([root])
    explored = set([root])
    while Q:
        node = Q.popleft()
        for edge in get_edges(node):
            if edge not in explored:
                Q.append(edge)
                explored.add(edge)
    print(list(Q), explored)
