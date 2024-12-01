from functools import cache, partial
import multiprocessing as mp
from itertools import combinations
from typing import Dict, List, Tuple

@cache
def parse_map(map: Tuple):
    galaxies = {}
    galaxy_count = 0
    no_galaxy = [set(),set()]
    for i, row in enumerate(map):
        if '#' not in row:
            no_galaxy[0].add(i)
        for j, col in enumerate(row):
            col_str = set(r[j] for r in map)
            if col == '#':
                galaxies[galaxy_count] = (i,j)
                galaxy_count += 1
                continue
            if '#' not in col_str:
                no_galaxy[1].add(j)

    return galaxies, no_galaxy
    
def get_distance(no_galaxy: List, galaxies: Dict, d: int, pair: Tuple):
    g2 = galaxies[pair[0]]
    g1 = galaxies[pair[1]]

    dx = abs(g1[1]-g2[1])
    dy = abs(g1[0]-g2[0])

    x1, x2 = sorted([g1[1], g2[1]])
    y1, y2 = sorted([g1[0], g2[0]])

    dx += d * len(set(range(x1, x2)) & no_galaxy[1])
    dy += d * len(set(range(y1, y2)) & no_galaxy[0])
    return dx + dy

def partA(input: str):
    map = input.splitlines()
    galaxies, no_galaxy = parse_map(tuple(map))

    pairs = list(combinations(range(len(galaxies)), 2))
    pool = mp.Pool(processes=16)
    return sum(pool.map(partial(get_distance, no_galaxy, galaxies, 1), pairs))
    
def partB(input: str):
    map = input.splitlines()
    galaxies, no_galaxy = parse_map(tuple(map))

    pairs = list(combinations(range(len(galaxies)), 2))
    pool = mp.Pool(processes=16)
    return sum(pool.map(partial(get_distance, no_galaxy, galaxies, 999_999), pairs))

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd11.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
