from collections import deque
from typing import List

def verify(map: str, counts: List):
    groups = deque([c for c in map.split('.') if c])
    if len(counts) != len(groups):
        return None
    for count in counts:
        group = groups.popleft()
        if count != len(group):
            return None
    return map

def partA(input: str):
    input = input.splitlines()
    sum = 0
    for p, line in enumerate(input):
        map, counts = line.split()
        counts = [int(c) for c in counts.split(',')]
        n_unknown = map.count('?')
        arrangements = set()
        print(f'{p+1} out of 1000', end='\r')
        for n in range(2**n_unknown):
            b = deque(c for c in f'{n:0>{n_unknown}b}'.replace('0', '.').replace('1', '#'))
            nmap = ''
            for c in map:
                if c == '?':
                    nmap += b.popleft()
                else:
                    nmap += c
            if (m := verify(nmap, counts)):
                arrangements.add(m)
        sum += len(arrangements)
    print()
    return sum

def partB(input: str):
    pass
if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd12.in'
    inp = open(infile).read().strip()
    # print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
