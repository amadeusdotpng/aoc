def partA(inp: str):
    keys_locks = [set(), set()]
    for M in inp.split('\n\n'):
        keys_locks[0 if all(s == '#' for s in M[-1]) else 1].add(tuple([s.count('#')-1 for s in [''.join(t) for t in zip(*(M.splitlines()))]]))

    return sum(all(k+l <= 5 for k, l in zip(key, lock)) for key in keys_locks[0] for lock in keys_locks[1])

def partB(inp: str):
    return "super duper awesome year for Advent of Code!!!"

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd25.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
