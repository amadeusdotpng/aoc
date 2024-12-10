from collections import deque
from itertools import zip_longest

def partA(inp: str):
    total = 0

    Q = deque([[id for _ in range(int(n))] for id, n in enumerate(inp[::2])])
    S = deque([int(n) for n in inp[1::2]])

    pos = 0
    empty = False

    while Q:
        if not empty:
            L = Q.popleft()
            for id in L:
                total += id * pos
                pos += 1

        if empty:
            s = S.popleft()
            L = Q.pop()
            while s > 0:
                total += pos * L.pop()

                if len(L) == 0:
                    L = Q.pop()

                pos += 1
                s -= 1
            if L:
                Q.append(L)
        empty = not empty
    return total



def rearrange(F):
    for i in range(len(F)-1, -1, -1):
        b_id, b_size = F[i]
        if b_id == -1:
            continue

        for j in range(i):
            # print(F[j], 'inner')
            e_id, e_size = F[j]
            if e_id != -1 or b_size > e_size:
                continue

            F[j] = F[i]
            F[i] = (-1, b_size)

            if i+1 < len(F) and F[i+1][0] == -1:
                _, n_size = F[i+1]
                _, t_size = F[i]
                F[i] = (-1, t_size + n_size)
                F[i+1] = (-1, 0)

            if i-1 < len(F) and F[i-1][0] == -1:
                _, n_size = F[i-1]
                _, t_size = F[i]
                F[i] = (-1, t_size + n_size)
                F[i-1] = (-1, 0)

            if e_size - b_size > 0:
                F.insert(j+1, (-1, e_size - b_size))

            # print(F)

            break

def partB(inp: str):
    total = 0

    Q = [(id, int(n)) for id, n in enumerate(inp[::2])]
    S = [(-1, int(n)) for n in inp[1::2]]
    
    F = [f for B in zip_longest(Q, S, fillvalue=None) for f in B if f]

    # print(F)
    rearrange(F)
    # print(F)

    pos = 0
    # s = ''
    for id, n in F:
        for _ in range(n):
            total += pos * (id if id >= 0 else 0)
            # s += f'{id}' if id >= 0 else '.'
            pos += 1
        # print(id, n, pos, total)
    # print(s)
    return total

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd09.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
