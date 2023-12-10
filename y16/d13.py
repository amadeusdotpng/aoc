from queue import Queue

def pathfind(bias: int, goal: complex):
    to_explore = Queue()
    root = 1+1j
    explored = set([root])
    parents = {}

    to_explore.put(root)
    while not to_explore.empty():
        node = to_explore.get()
        if node == goal:
            return get_path(parents, node, root)
        for edge in get_edges(node):
            if edge in explored:
                continue
            explored.add(edge)
            if int(edge.real) < 0 or int(edge.imag) < 0:
                continue
            if validate(edge, bias):
                parents[edge] = node
                to_explore.put(edge)
            
def validate(node: complex, bias: int):
    x, y = int(node.real), int(node.imag)
    binary = x*x + 3*x + 2*x*y + y + y*y + bias
    count = 0
    while binary:
        count += binary & 1
        binary >>= 1
    return not (count % 2)
        
def get_edges(node: complex):
    return [node-1j, node+1, node+1j, node-1]

def get_path(parents: dict, node: complex, root: complex):
    path = set()
    while node != root:
        node = parents[node]
        path.add(node)
    return path
    

def partA(input: str):
    path = pathfind(int(input), 31+39j)
    return len(path)


def partB(bias: str):
    to_explore = Queue()
    root = 1+1j
    explored = set([root])
    parents = {}

    to_explore.put(root)
    while not to_explore.empty():
        node = to_explore.get()
        explored.add(node)
        for edge in get_edges(node):
            if edge in explored:
                continue
            if int(edge.real) < 0 or int(edge.imag) < 0:
                continue
            if len(get_path(parents, node, root)) < 50:
                if validate(edge, int(bias)):
                    parents[edge] = node
                    to_explore.put(edge)
    return len(explored)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd13.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
