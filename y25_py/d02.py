import re
from math import ceil

def partA(inp: str):
    rs = [tuple([id for id in r.split('-')]) for r in inp.split(',')]
    C = 0
    for (l, r) in rs:
        if len(l) == len(r) and len(l) % 2 == 1: continue
        hl, hr = l[:len(l)//2], r[:ceil(len(r)/2)]
        hl = int(hl) if hl else 0
        hr = int(hr) if hr else 0
        for h in range(hl, hr+1):
            n = int(2*str(h))
            if int(l) <= n <= int(r):
                C += n
    return C



def partB(inp: str):
    rs = [tuple([id for id in r.split('-')]) for r in inp.split(',')]
    C = 0
    for (l, r) in rs:
        sl = 1
        sr = max(int(l[:ceil(len(l)/2)+1]), int(r[:ceil(len(r)/2)+1]))
        cache = set()
        for s in range(sl,sr+1):
            for k in range(len(l), len(r)+1):
                k = ceil(k/len(str(s)))
                if k == 1: continue
                n = int(k*str(s))
                if int(l) <= n <= int(r) and n not in cache:
                    cache.add(n)
                    C += n
    return C

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd02.in'
    inp = open(infile).read().strip()
    # print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
