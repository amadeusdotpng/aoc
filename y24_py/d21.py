from itertools import permutations, pairwise
from functools import lru_cache
import re

NUMPAD_COORDS = {
    'A': 3+2j,
    '0': 3+1j,
    '3': 2+2j,
    '2': 2+1j,
    '1': 2+0j,
    '6': 1+2j,
    '5': 1+1j,
    '4': 1+0j,
    '9': 0+2j,
    '8': 0+1j,
    '7': 0+0j,
}

KEYPAD_COORDS = {
    '>': 1+2j,
    'v': 1+1j,
    '<': 1+0j,
    '^': 0+1j,
    'A': 0+2j,
}

def ints(s):
    return [int(n) for n in re.findall(r'\d+', s)]

def get_numpad_sequences(f, t):
    assert f in NUMPAD_COORDS
    assert t in NUMPAD_COORDS
    fs = NUMPAD_COORDS[f]
    ts = NUMPAD_COORDS[t]
    d = ts - fs
    ud = ('v' if d.real > 0 else '^') * int(abs(d.real))
    lr = ('>' if d.imag > 0 else '<') * int(abs(d.imag))
    udlr = ud+lr
    return {
        s+'A' for s in map(lambda t: ''.join(t), permutations(udlr, len(udlr)))
        if not (
            (f == '7' and s.startswith('vvv')) or
            (f == '4' and s.startswith('vv' )) or
            (f == '1' and s.startswith('v'  )) or
            (f == 'A' and s.startswith('<<' )) or
            (f == '0' and s.startswith('<'  ))
        )
    }

def get_keypad_sequences(f, t):
    assert f in KEYPAD_COORDS
    assert t in KEYPAD_COORDS
    fs = KEYPAD_COORDS[f]
    ts = KEYPAD_COORDS[t]
    d = ts - fs
    ud = ('v' if d.real > 0 else '^') * int(abs(d.real))
    lr = ('>' if d.imag > 0 else '<') * int(abs(d.imag))
    udlr = ud+lr
    return {
        s+'A' for s in map(lambda t: ''.join(t), permutations(udlr, len(udlr)))
        if not (
            (f == '<' and s.startswith('^' )) or
            (f == 'A' and s.startswith('<<')) or
            (f == '^' and s.startswith('<' ))
        )
    }

def get_length(code, layers):
    @lru_cache(None)
    def f(s, layer):
        if layer == layers:
            return len(s)

        return sum(min(f(seq, layer+1) for seq in get_keypad_sequences(a, b)) for a, b, in pairwise('A'+s) )

    return sum(min(f(seq, 0) for seq in get_numpad_sequences(a, b)) for a, b in pairwise('A'+code))

def partA(inp: str):
    return sum(int(code[:-1]) * get_length(code, 2) for code in inp.splitlines())
    
def partB(inp: str):
    return sum(int(code[:-1]) * get_length(code, 25) for code in inp.splitlines())

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd21.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
