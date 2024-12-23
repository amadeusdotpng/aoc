from collections import defaultdict, deque

def run(root, goal, B, R, C):
    Q = deque([(0, root)])
    X = {root}
    touched_B = set()

    get_edges = lambda r, c: [
        (r+dr, c+dc) for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if 0 <= r+dr <= R and 0 <= c+dc <= C
    ]
    while Q:
        ncost, (nr, nc) = Q.popleft()

        if (nr, nc) == goal:
            return touched_B, ncost

        for e in get_edges(nr, nc):
            ecost = ncost + 1

            if e in X:
                continue

            if e in B:
                touched_B.add(e)
                continue

            Q.append((ecost, e))
            X.add(e)

def partA(inp: str):
    M = inp.splitlines()
    B = set()
    R, C = len(M)-1, len(M[0])-1
    root = None
    goal = None
    for r, line in enumerate(M):
        for c, char in enumerate(line):
            if char == 'S': root = (r, c)
            if char == 'E': goal = (r, c)
            if char == '#': B.add((r, c))

    touched_B, normal_runtime = run(root, goal, B, R, C)

    S = 0
    print(len(touched_B), len(B))
    for i, b in enumerate(touched_B):
        if i % 25 == 0: print(i, end='\r')
        _, runtime = run(root, goal, B-{b}, R, C)
        if normal_runtime - runtime >= 100: S += 1

    print()
    return S


def get_cheated_costs(p, normal_costs, O, R, C):
    Q = deque([(20, 0, p)])
    X = set()
    cheated_positions = dict()

    get_edges = lambda p: [
        p+d for d in [-1, 1j, 1, -1j]
        if 0 <= (p+d).real <= R and 0 <= (p+d).real <= C
    ]

    while Q:
        lifetime, cost, n = Q.popleft()

        if n in O and n != p:
            if normal_costs[n] != cost:
                cheated_positions[n] = cost

        for e in get_edges(n):
            elifetime = lifetime-1

            if e in X: continue
            if elifetime < 0: continue

            Q.append((lifetime-1, cost+1, e))
            X.add(e)

    return cheated_positions

def get_position_costs(p, g, B, R, C):
    Q = deque([(0, p)])
    X = {p}
    costs = dict()

    get_edges = lambda p: [
        p+d for d in [-1+0j, 0+1j, 1+0j, 0-1j]
        if 0 <= (p+d).real <= R and 0 <= (p+d).real <= C
    ]

    while Q:
        ncost, n = Q.popleft()
        costs[n] = ncost

        if n == g:
            return costs

        for e in get_edges(n):
            ecost = ncost + 1
            if e in B: continue
            if e in X: continue

            Q.append((ecost, e))
            X.add(e)

def partB(inp: str):
    M = inp.splitlines()
    B = set()
    O = set()
    R, C = len(M)-1, len(M[0])-1
    root = None
    goal = None
    for r, line in enumerate(M):
        for c, char in enumerate(line):
            if char == 'S': root = complex(r, c)
            if char == 'E': goal = complex(r, c)
            if char == '#': B.add(complex(r, c))
            if char == '.': O.add(complex(r, c))

    O.add(root)
    O.add(goal)

    S = 0
    normal_costs = get_position_costs(root, goal, B, R, C)
    # AAA = defaultdict(int)
    for idx, o in enumerate(O):
        if idx % 5 == 0:
            print(f'{idx} / {len(O)}', end='\r')

        cheated_costs = get_cheated_costs(o, normal_costs, O, R, C)
        '''
        if o == 3+1j:
            print(o, cheated_positions)
        '''
        ocost = normal_costs[o]

        for p in cheated_costs:
            pcost = cheated_costs[p]
            '''
            if o == 7+8j and p == 9+8j:
                print(normal_costs[goal], normal_costs[p], ocost, pcost)
                print(normal_costs[goal] - (normal_costs[goal] - (normal_costs[p] - ocost) + pcost))
            '''
            saved_cost = normal_costs[goal] - (normal_costs[goal] - (normal_costs[p] - ocost) + pcost)
            if saved_cost >= 100:
                # AAA[saved_cost] += 1
                S += 1

    # __import__('pprint').pprint(AAA)

    print()
    return S

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd20.in'
    inp = open(infile).read().strip()
    # print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')



    '''
        print(n, g)
        print(
            '\n'.join(
                ''.join(
                    '#' if complex(r, c) in B else
                    'O' if complex(r, c) == n else
                    'S' if complex(r, c) == p else
                    'E' if complex(r, c) == g else
                    '.'
                    for c in range(C+1)
                )
                for r in range(R+1)
            )
        )
    '''
