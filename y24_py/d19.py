from functools import cache

@cache
def verify(P, t, part):
    t_l = len(t)

    if t_l == 0:
        return 1

    if t_l == 1:
            return 1 if t in P else 0

    if part == 'A': return any(verify(P, t[len(p):], part) for p in P if p == t[:len(p)])
    if part == 'B': return sum(verify(P, t[len(p):], part) for p in P if p == t[:len(p)])

def partA(inp: str):
    P, T = inp.split('\n\n')
    P = tuple(reversed(sorted(P.split(', '), key=lambda s: len(s))))
    T = T.splitlines()

    return sum(verify(P, t, 'A') for t in T)

    # verify = cache(lambda t: 1 if len(t) == 0 else t in P if len(t) == 1 else any(solve(t[len(p):]) for p in P if p == t[:len(p)]))
    # return sum(verify(t) for t in T)

def partB(inp: str):
    P, T = inp.split('\n\n')
    P = tuple(reversed(sorted(P.split(', '), key=lambda s: len(s))))
    T = T.splitlines()

    return sum(verify(P, t, 'B') for t in T)

    # verify = cache(lambda t: 1 if len(t) == 0 else t in P if len(t) == 1 else sum(solve(t[len(p):]) for p in P if p == t[:len(p)]))
    # return sum(verify(t) for t in T)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd19.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')

