from itertools import combinations

def partA(inp: str):
    r_ids, ids = inp.split('\n\n')
    r_ids, ids = [tuple(map(int, r_id.split('-'))) for r_id in r_ids.split('\n')], [int(id) for id in ids.split('\n')]
    return len({id for id in ids for l, r in r_ids if l <= id <= r})


def partB(inp: str):
    C = 0

    r_ids, _ = inp.split('\n\n')
    r_ids = {tuple(map(int, r_id.split('-'))) for r_id in r_ids.split('\n')}
        
    while True:
        nr_ids = set()
        merged, not_merged = set(), set()
        for (al, ar), (bl, br) in combinations(r_ids, 2):
            if not (al > br or ar < bl):
                merged.add((al, ar))
                merged.add((bl, br))
                nr_ids.add((min(al, bl), max(ar, br)))
                continue
            not_merged.add((al, ar))
            not_merged.add((bl, br))

        if not merged:
            break
        r_ids = nr_ids | (not_merged - merged)

    for (l, r) in r_ids:
        C += r - l + 1

    return C

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd05.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
