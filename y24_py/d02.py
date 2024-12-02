def verify(L):
    dir = 1 if L[0] - L[1] < 0 else -1
    cmp = lambda i, j: 1 <= abs(L[i] - L[j]) <= 3 and ((dir == 1 and L[i] - L[j] < 0) or (dir == -1 and L[i] - L[j] > 0))
    for k in range(len(L)-1):
        valid = cmp(k, k+1)
        if not valid: return False

    return True


def partA(inp: str):
    I = [list(map(int, line.split())) for line in inp.splitlines()]
    return sum(
        map(lambda line: verify(line), I)
    )

def partB(inp: str):
    I = [list(map(int, line.split())) for line in inp.splitlines()]
    return sum(
        map(lambda line: verify(line) or any(verify(line[:i]+line[i+1:]) for i in range(len(line))), I)
    )

# finding out what was wrong with my first attempt
'''
def verify2(L):
    dir = 1 if L[0] - L[1] < 0 else -1
    cmp = lambda i, j: 1 <= abs(L[i] - L[j]) <= 3 and ((dir == 1 and L[i] - L[j] < 0) or (dir == -1 and L[i] - L[j] > 0))
    for k in range(len(L)-1):
        valid = cmp(k, k+1)
        if not valid: return k, k+1, False

    return None, None, True

def partC(inp: str):
    I = [tuple(map(int, line.split())) for line in inp.splitlines()]
    incorrect = set()
    for line in I:
        i, j, r = verify2(line)
        if not r:
            one, two = verify2(line[:i]+line[i+1:])[-1], verify2(line[:j]+line[j+1:])[-1]
            r = one or two

        if line == (39, 37, 39, 42, 44, 46, 48):
            print(line, i, j, line[:i]+line[i+1:], line[:j]+line[j+1:], one, two)

        if r:
            incorrect.add(line)
    correct = set(
        filter(lambda line: verify(line) or any(verify(line[:i]+line[i+1:]) for i in range(len(line))), I)
    )
    return '\n'+'\n'.join(str(S) for S in correct-incorrect)
'''
        
if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd02.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
    # print(f'C: {partC(inp[::])}')

