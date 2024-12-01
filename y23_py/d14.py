from functools import cache
from typing import List

def tiltCol(col: str) -> str:
    return '#'.join('O'*S.count('O')+S.replace('O', '') for S in col.split('#'))[::-1]

def transpose(map: str, tilt: bool) -> str:
    L = [tiltCol(''.join(s)) if tilt else ''.join(s)[::-1] for s in zip(*map.splitlines())]
    return '\n'.join(L)

def getLoadCol(col: str) -> int:
    return sum(i+1 for i,c in enumerate(col) if c == 'O')

def getLoadMap(map: str):
    map = map.splitlines()
    sum= 0
    for i in range(len(map[0])):
        col = ''
        for row in map:
            col += row[i]
        sum += getLoadCol(col[::-1])
    return sum

def partA(input: str):
    map = transpose(input, tilt=True)
    for _ in range(3):
        map = transpose(map, tilt=False)
    return getLoadMap(map)

def cycle(map: str) -> str:
    map = transpose(map, tilt=True)
    map = transpose(map, tilt=True)
    map = transpose(map, tilt=True)
    return transpose(map, tilt=True)

def partB(input: str):
    map = input
    i = 1
    map_to_index = {map:0}
    index_to_map = {0:map}
    while True:
        map = cycle(map)
        if map in map_to_index:
            break
        map_to_index[map] = i
        index_to_map[i] = map
        i += 1
    return getLoadMap(index_to_map[map_to_index[map]+(1_000_000_000-map_to_index[map])%(len(map_to_index)-map_to_index[map])])


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd14.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
