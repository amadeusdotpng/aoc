from collections import deque

def run(L, blocks):
    root = 0+0j
    goal = complex(L,L)
    
    Q = deque([(root, [])])
    X = set()

    get_edges = lambda p: [
        p+d for d in [0-1j, 1+0j, 0+1j, -1+0j] 
        if 0 <= (p+d).real <= L and 0 <= (p+d).imag <= L
    ]

    while Q:
        n, npath = Q.popleft()
        if n == goal:
            return len(npath)

        for e in get_edges(n):
            if e in X:
                continue

            if e in blocks:
                continue
            
            Q.append((e, npath + [e]))
            X.add(e)

def partA(inp: str):
    blocks = list(complex( *(map(int, n.split(','))) ) for n in inp.splitlines()[:1024])

    L = 70
    res = run(L, blocks)
    return res

def partB(inp: str):
    blocks = list(complex( *(map(int, n.split(','))) ) for n in inp.splitlines())

    L = 70
    current_blocks = set()

    for block in blocks:
        current_blocks.add(block)
        if run(L, current_blocks) is None:
            return f'{int(block.real)},{int(block.imag)}'

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd18.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
