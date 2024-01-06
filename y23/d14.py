from functools import cache
from typing import List

def cycle(map: str) -> str:
    map = tiltMap(map)
    map = tiltMap(map)
    map = tiltMap(map)
    return tiltMap(map)

def tiltMap(map: str) -> str:
    map = map.splitlines()
    out = []
    for i in range(len(map[0])):
        col = ''
        for row in map:
            col += row[i]
        out.append(tiltCol(col))
    return '\n'.join(out)

def tiltCol(col: str) -> str:
    return '#'.join('O'*S.count('O')+S.replace('O', '') for S in col.split('#'))[::-1]

def getLoadMap(map: str):
    map = map.splitlines()
    sum= 0
    for i in range(len(map[0])):
        col = ''
        for row in map:
            col += row[i]
        sum += getLoadCol(col[::-1])
    return sum

def getLoadCol(col: str) -> int:
    return sum(i+1 for i,c in enumerate(col) if c == 'O')

def transpose(map: str) -> str:
    map = map.splitlines()
    L = []
    for i in range(len(map[0])):
        col = ''
        for row in map:
            col += row[i]
        L.append(col[::-1])
    return '\n'.join(L)

def partA(input: str):
    map = tiltMap(input)
    for _ in range(3):
        map = transpose(map)
    return getLoadMap(map)

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
        # print(f'{i}\n'+next+'\n')
        i += 1
    print(len(map_to_index)-map_to_index[map])
    return getLoadMap(index_to_map[map_to_index[map]+(1_000_000_000-map_to_index[map])%(len(map_to_index)-map_to_index[map])])

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd14.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
