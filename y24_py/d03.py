def partA(inp: str):
    S = 0
    parseString = lambda state, s: (state[len(s):], True) if state[:len(s)] == s else (state[1:], False)

    _parseNum = lambda state, acc:  (state, acc) if not state[0].isdigit() else _parseNum(state[1:], acc+state[0])
    parseNum  = lambda state: _parseNum(state, '')

    while inp:
        inp, res = parseString(inp, 'mul(')
        if not res:
            continue

        inp, x = parseNum(inp)
        if not x:
            continue
        x = int(x)

        inp, res = parseString(inp, ',')
        if not res:
            continue

        inp, y = parseNum(inp)
        if not y:
            continue
        y = int(y)

        inp, res = parseString(inp, ')')
        if not res:
            continue

        S += x * y

    return S

def partB(inp: str):
    S = 0
    do = True
    parseString = lambda state, s: (state[len(s):], True) if state[:len(s)] == s else (state[1:], False)

    _parseNum = lambda state, acc:  (state, acc) if not state[0].isdigit() else _parseNum(state[1:], acc+state[0])
    parseNum  = lambda state: _parseNum(state, '')

    while inp:
        _, res = parseString(inp, 'do()')
        if res:
            do = True

        _, res = parseString(inp, 'don\'t()')
        if res:
            do = False

        inp, res = parseString(inp, 'mul(')
        if not res:
            continue

        inp, x = parseNum(inp)
        if not x:
            continue
        x = int(x)

        inp, res = parseString(inp, ',')
        if not res:
            continue

        inp, y = parseNum(inp)
        if not y:
            continue
        y = int(y)

        inp, res = parseString(inp, ')')
        if not res:
            continue

        if do:
            S += x * y

    return S

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd03.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
