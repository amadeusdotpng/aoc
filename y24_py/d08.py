from collections import defaultdict

def partA(inp: str):
    inp = inp.splitlines()

    W, H = len(inp)-1, len(inp[0])-1

    in_bounds = lambda p: 0 <= p[0] <= H and 0 <= p[1] <= W
    all_antennas = set()
    antennas = defaultdict(set)
    for r, line in enumerate(inp):
        for c, char in enumerate(line):
            if char != '.':
                antennas[char].add((r, c))
                all_antennas.add((r, c))

    antinodes = set()
    for k_antenna in antennas:
        s_antenna = antennas[k_antenna]
        for A in s_antenna:
            for B in s_antenna:
                if A == B: continue
                r_a, c_a = A
                r_b, c_b = B
                r_d, c_d = (r_a - r_b, c_a - c_b)

                a_p, a_m = (r_a - r_d, c_a - c_d), (r_a + r_d, c_a + c_d)
                b_p, b_m = (r_b - r_d, c_b - c_d), (r_b + r_d, c_b + c_d)
                # print(a_p, a_m, b_p, b_m)
                if a_p not in s_antenna and in_bounds(a_p): antinodes.add(a_p)
                if a_p not in s_antenna and in_bounds(a_m): antinodes.add(a_m)
                if b_p not in s_antenna and in_bounds(b_p): antinodes.add(b_p)
                if b_m not in s_antenna and in_bounds(b_m): antinodes.add(b_m)

    print('  000000000011')
    print('  012345678901')
    for r in range(W+1):
        s = f'{r:0>2}'
        for c in range(H+1):
            if (r, c) in all_antennas:
                s += 'A'
            elif (r, c) in antinodes:
                s += '#'
            else:
                s += '.'
        print(s)
    print(antinodes)
    return len(antinodes)


def partB(inp: str):
    inp = inp.splitlines()

    W, H = len(inp)-1, len(inp[0])-1

    in_bounds = lambda p: 0 <= p[0] <= H and 0 <= p[1] <= W
    all_antennas = set()
    antennas = defaultdict(set)
    for r, line in enumerate(inp):
        for c, char in enumerate(line):
            if char != '.':
                antennas[char].add((r, c))
                all_antennas.add((r, c))

    antinodes = set()
    for k_antenna in antennas:
        s_antenna = antennas[k_antenna]
        for A in s_antenna:
            for B in s_antenna:
                if A == B: continue
                r_a, c_a = A
                r_b, c_b = B

                # delta
                r_d, c_d = (r_a - r_b, c_a - c_b)

                r_s, c_s = A
                while in_bounds((r_s, c_s)):
                    antinodes.add((r_s, c_s))
                    r_s, c_s = r_s + r_d, c_s + c_d

                r_s, c_s = A
                while in_bounds((r_s, c_s)):
                    antinodes.add((r_s, c_s))
                    r_s, c_s = r_s - r_d, c_s - c_d
                
                '''
                a_p, a_m = (r_a - r_d, c_a - c_d), (r_a + r_d, c_a + c_d)
                b_p, b_m = (r_b - r_d, c_b - c_d), (r_b + r_d, c_b + c_d)
                if a_p not in s_antenna and in_bounds(a_p): antinodes.add(a_p)
                if a_p not in s_antenna and in_bounds(a_m): antinodes.add(a_m)
                if b_p not in s_antenna and in_bounds(b_p): antinodes.add(b_p)
                if b_m not in s_antenna and in_bounds(b_m): antinodes.add(b_m)
                '''

    print('  000000000011')
    print('  012345678901')
    for r in range(W+1):
        s = f'{r:0>2}'
        for c in range(H+1):
            if (r, c) in all_antennas:
                s += 'A'
            elif (r, c) in antinodes:
                s += '#'
            else:
                s += '.'
        print(s)
    print(antinodes)
    return len(antinodes)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd08.in'
    inp = open(infile).read().strip()
    # print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
