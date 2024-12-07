from itertools import chain, product, zip_longest
from math import gcd

def partA(inp: str):
    S = 0
    for line in inp.splitlines():
        eq, rest = line.split(': ')
        eq = int(eq)
        vals = list(map(int, rest.split()))
        for k in range(2 ** (len(vals)-1)):
            N = vals[::]
            mask = 1
            ops = []
            while mask < 2 ** (len(N)-1):
                if mask & k: ops.append('*')
                else: ops.append('+')
                mask <<= 1

            stack = []
            while len(N) > 0:
                stack.append(N.pop(0))
                if len(stack) == 2:
                    lhs = stack.pop(0)
                    rhs = stack.pop(0)
                    op = ops.pop(0)
                    if op == '*': stack.append(lhs * rhs)
                    else: stack.append(lhs + rhs)
            if stack[0] == eq:
                S += eq
                break
    return S
            
def partB(inp: str):
    S = 0
    inp = inp.splitlines()
    L = len(inp)
    for i, line in enumerate(inp):
        print(f'{i}/{L}', end='\r')
        eq, rest = line.split(': ')
        eq = int(eq)
        vals = list(map(int, rest.split()))
        for o in product(r'+*\|', repeat=len(vals) - 1):
            N = vals[::]
            ops = [c for c in o]

            while len(N) > 1:
                lhs = N.pop(0)
                rhs = N.pop(0)
                op = ops.pop(0)
                if op == '+': N.insert(0, lhs + rhs)
                elif op == '*': N.insert(0, lhs * rhs)
                else: N.insert(0, int(str(lhs) + str(rhs)))

            if N[0] == eq:
                S += eq
                break
    return S

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd07.in'
    inp = open(infile).read().strip()
    # print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
