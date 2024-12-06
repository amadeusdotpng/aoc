def partA(inp: str):
    return sum(1 if c == '(' else -1 for c in inp)


def partB(inp: str):
    F = 0
    for i, c in enumerate(inp):
        F += 1 if c == '(' else -1
        if F == -1:
            return i+1

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd01.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
