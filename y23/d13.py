from typing import List

def checkEquivalence(pairs: zip, part2: bool) -> bool:
    if part2:
        smudged = False
        for a,b in [c_pair for s_pair in pairs for c_pair in zip(s_pair[0], s_pair[1])]:
            if a != b and not smudged:
                smudged = True
            elif a != b and smudged:
                return False
        return smudged
    else:
        return all(a==b for a,b, in pairs)

def checkReflection(map: List, part2: bool) -> int:
    L = len(map)
    for n in range(1,L):
        above = map[max(0,n-min(n,L-n)):n]
        below = reversed(map[n:min(L, n+min(n,L-n))])
        if checkEquivalence(zip(above, below), part2):
            return n
    return 0

def transposeMap(map: List) -> List:
    L = []
    for col in range(len(map[0])):
        buf = ''
        for row in map:
            buf += row[col]
        L.append(buf)
    return L


def partA(input: str) -> int:
    maps = [line.split() for line in input.split('\n\n')]
    sum = 0
    for map in maps:
        if (n := checkReflection(map, part2=False)):
            sum += n * 100
        else:
            sum += checkReflection(transposeMap(map), part2=False)
    return sum

def partB(input: str) -> int:
    maps = [line.split() for line in input.split('\n\n')]
    sum = 0
    for map in maps:
        if (n := checkReflection(map, part2=True)):
            sum += n * 100
        else:
            sum += checkReflection(transposeMap(map), part2=True)
    return sum


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd13.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
