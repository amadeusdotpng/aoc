from typing import Dict, Set, Tuple

from dataclasses import dataclass
import itertools

@dataclass
class Point:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

@dataclass
class Block:
    l: Point
    r: Point
    name: str | None

    TuplePoint = Tuple[int, int, int]
    def __init__(self, l: TuplePoint | Point, r: TuplePoint | Point, name: str | None = None):
        if isinstance(l, Tuple): self.l = Point(*l)
        else: self.l = l

        if isinstance(r, Tuple): self.r = Point(*r)
        else: self.r = r

        if name is None:
            self.name = f'{self.l}, {self.r}'
        else:
            self.name = name

    def __hash__(self):
        return hash((self.l, self.r))

    def __repr__(self):
        return self.name

    def __str__(self):
        return str(self.name)

def will_collide(A: Block, B: Block):
    return (
        A.l.y <= B.r.y and
        A.r.y >= B.l.y and
        A.l.x <= B.r.x and
        A.r.x >= B.l.x
    )

def get_supports(c_block: Block, blocks_r: Dict[int, Set[Block]]) -> Tuple[Set[Block], int] | None:
    from_z = c_block.l.z
    for to_z in range(from_z-1, 0, -1):
        if to_z not in blocks_r:
            continue

        supported_by = { o_block for o_block in blocks_r[to_z] if will_collide(c_block, o_block) }
        
        if supported_by:
            return supported_by, to_z + 1

    return set(), 1

def partA(inp: str):
    blocks_l: Dict[int, Set[Block]] = {} # key is lowest z level of block
    blocks_r: Dict[int, Set[Block]] = {} # key is highest z level of block

    supports: Dict[Block, Set[Block]] = {}
    in_degree: Dict[Block, int] = {}

    for line in inp.splitlines():
        l, r = line.split('~')
        lx, ly, lz = (int(n) for n in l.split(','))
        rx, ry, rz = (int(n) for n in r.split(','))

        # make sure that l values is always less than or equal to r values
        assert lx <= rx and ly <= ry and lz <= rz

        if lz not in blocks_l:
            blocks_l[lz] = set()

        if rz not in blocks_r:
            blocks_r[rz] = set()

        block = Block(
            (lx, ly, lz),
            (rx, ry, rz),
        )

        blocks_l[lz].add(block)
        blocks_r[rz].add(block)

    for from_z in sorted(blocks_l.copy().keys()):
        if from_z == 1:
            continue

        for c_block in blocks_l[from_z].copy():
            supported_by, to_z = get_supports(c_block, blocks_r)

            lx, ly, lz = c_block.l
            rx, ry, rz = c_block.r
            dz = max(lz, rz) - min(lz, rz)

            blocks_l[lz].remove(c_block)
            blocks_r[rz].remove(c_block)

            if to_z not in blocks_l:
                blocks_l[to_z] = set()

            if to_z + dz not in blocks_r:
                blocks_r[to_z + dz] = set()

            c_block = Block((lx, ly, to_z), (rx, ry, to_z + dz), c_block.name)
            blocks_l[to_z].add( c_block )
            blocks_r[to_z + dz].add( c_block )

            in_degree[c_block] = len(supported_by) if supported_by else 1

            for s_block in supported_by:
                if s_block not in supports:
                    supports[s_block] = set()

                supports[s_block].add(c_block)


    count = 0
    for s_block in itertools.chain(*blocks_l.values()):
        if s_block in supports and any(in_degree[B] - 1 == 0 for B in supports[s_block]):
            continue

        count += 1
    return count

from collections import deque

def disintegrate(s_block: Block, supports: Dict[Block, Set[Block]], in_degree: Dict[Block, int]):
    count = 0
    # print(f'starting {s_block}')

    if s_block not in supports:
        # print(f'{s_block} does not support any other block!')
        return 0

    Q = deque([*supports[s_block]])
    # print(Q)
    while Q:
        node = Q.pop()

        in_degree[node] -= 1

        if in_degree[node] == 0:
            # print(node)
            count += 1
            
            if node not in supports:
                continue

            for edge in supports[node]:
                Q.append(edge)

    return count

def partB(inp: str):
    blocks_l: Dict[int, Set[Block]] = {} # key is lowest z level of block
    blocks_r: Dict[int, Set[Block]] = {} # key is highest z level of block

    supports: Dict[Block, Set[Block]] = {}
    in_degree: Dict[Block, int] = {}

    for line in inp.splitlines():
        l, r = line.split('~')
        lx, ly, lz = (int(n) for n in l.split(','))
        rx, ry, rz = (int(n) for n in r.split(','))

        # make sure that l values is always less than or equal to r values
        assert lx <= rx and ly <= ry and lz <= rz

        if lz not in blocks_l:
            blocks_l[lz] = set()

        if rz not in blocks_r:
            blocks_r[rz] = set()

        block = Block(
            (lx, ly, lz),
            (rx, ry, rz),
        )

        blocks_l[lz].add(block)
        blocks_r[rz].add(block)

    for from_z in sorted(blocks_l.copy().keys()):
        if from_z == 1:
            continue

        for c_block in blocks_l[from_z].copy():
            supported_by, to_z = get_supports(c_block, blocks_r)

            lx, ly, lz = c_block.l
            rx, ry, rz = c_block.r
            dz = max(lz, rz) - min(lz, rz)

            blocks_l[lz].remove(c_block)
            blocks_r[rz].remove(c_block)

            if to_z not in blocks_l:
                blocks_l[to_z] = set()

            if to_z + dz not in blocks_r:
                blocks_r[to_z + dz] = set()

            c_block = Block((lx, ly, to_z), (rx, ry, to_z + dz), c_block.name)
            blocks_l[to_z].add( c_block )
            blocks_r[to_z + dz].add( c_block )

            in_degree[c_block] = len(supported_by) if supported_by else 1

            for s_block in supported_by:
                if s_block not in supports:
                    supports[s_block] = set()

                supports[s_block].add(c_block)

    # __import__('pprint').pprint(supports)
    # __import__('pprint').pprint(in_degree)

    count = 0
    for s_block in itertools.chain(*blocks_l.values()):
        t = disintegrate(s_block, supports, in_degree.copy())
        # print(s_block, t)
        # print()
        count += t

    return count



if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd22.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
