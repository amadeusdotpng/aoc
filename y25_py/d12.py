from functools import cache

def parse(inp: str):
    inp_sp = inp.split('\n\n')
    P = tuple(tuple(s.split(':\n')[1].split('\n')) for s in inp_sp[:6])
    R = [
        tuple(line.split(': '))
        for line in inp_sp[-1].split('\n')
    ]
    R = [(tuple(map(int, r.split('x'))), tuple(map(int, N.split()))) for r, N in R]
    return P, R

def partA(inp):
    return sum(w*l >= 9*sum(N) for (w, l), N in inp[1])

def partB(inp):
    pass

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd12.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(parse(inp[::]))}')
    print(f'B: {partB(parse(inp[::]))}')
