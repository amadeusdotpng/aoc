from collections import defaultdict, deque

def partA(inp: str):
    adj_list = defaultdict(set)
    for line in inp.splitlines():
        a, b = line.split('-')
        adj_list[a].add(b)
        adj_list[b].add(a)

    interconnected = set()
    for n in adj_list:
        n_edges = adj_list[n]
        for e in n_edges:
            e_edges = adj_list[e]
            for common in (n_edges & e_edges):
                interconnected.add(frozenset((n, e, common)))

    return sum(any(computer[0] == 't' for computer in fset) for fset in interconnected)

def find_biggest(root, adj_list):
    Q = deque([(root, {root})])
    X = set()
    seen_sets = set()

    is_connected = lambda a, b: a in adj_list[b] and b in adj_list[a]

    best_set = None

    while Q:
        n, interconnected = Q.popleft()

        if best_set is None or len(best_set) < len(interconnected):
            best_set = interconnected

        for e in adj_list[n]:
            new_interconnected = interconnected | {e}

            if new_interconnected in seen_sets:
                continue

            if not all(is_connected(e, o) for o in interconnected if e != o):
                continue

            Q.append((e, new_interconnected))
            X.add(e)
            seen_sets.add(frozenset(new_interconnected))


    return best_set, X


def partB(inp: str):
    adj_list = defaultdict(set)
    for line in inp.splitlines():
        root, b = line.split('-')
        adj_list[root].add(b)
        adj_list[b].add(root)

    seen = set()
    best_set = set()
    for root in adj_list:
        if root in seen:
            continue

        best_root, seen_root = find_biggest(root, adj_list)
        seen |= seen_root

        if len(best_set) < len(best_root):
            best_set = best_root

    best_set = ','.join(sorted(best_set))
    return best_set

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd23.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
