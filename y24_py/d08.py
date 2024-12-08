from collections import defaultdict
from itertools import product

def partA(inp: str):
    inp = inp.splitlines()
    W, H = len(inp)-1, len(inp[0])-1

    in_bounds = lambda p: 0 <= p.real <= H and 0 <= p.imag <= W

    frequencies = defaultdict(set)
    for r, line in enumerate(inp):
        for c, char in enumerate(line):
            if char != '.':
                frequencies[char].add(complex(r, c))

    antinodes = set()
    for antennas in frequencies.values():
        for (f, t) in product(antennas, repeat=2):
            if f == t: continue

            d = t - f
            an = f + 2 * d

            if in_bounds(an):
                antinodes.add(an)

    return len(antinodes)

def partB(inp: str):
    inp = inp.splitlines()
    W, H = len(inp)-1, len(inp[0])-1

    in_bounds = lambda p: 0 <= p.real <= H and 0 <= p.imag <= W

    frequencies = defaultdict(set)
    for r, line in enumerate(inp):
        for c, char in enumerate(line):
            if char != '.':
                frequencies[char].add(complex(r, c))

    antinodes = set()
    for antennas in frequencies.values():
        for (f, t) in product(antennas, repeat=2):
            if f == t: continue

            d = t - f
            an = f + d

            while in_bounds(an):
                antinodes.add(an)
                an += d

    return len(antinodes)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd08.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
