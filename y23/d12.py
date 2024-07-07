from collections import deque
from functools import cache
from typing import List, Tuple


def verify(map: str, counts: List):
    groups = deque([c for c in map.split(".") if c])
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
        record, counts = line.split()
        counts = [int(c) for c in counts.split(",")]
        n_unknown = record.count("?")
        arrangements = set()
        print(f"{p+1} out of 1000", end="\r")
        for n in range(2**n_unknown):
            b = [c for c in f"{n:0>{n_unknown}b}".replace("0", ".").replace("1", "#")]
            nrecord = ""
            for c in record:
                if c == "?":
                    nrecord += b.popleft()
                else:
                    nrecord += c
            if m := verify(nrecord, counts):
                arrangements.add(m)
        sum += len(arrangements)
    print()
    return sum

def partB(input: str):
    N = 5
    input = input.splitlines()
    sum = 0

    for p, line in enumerate(input):
        record, counts = line.split()

        record = "?".join(record for _ in range(N))
        counts = tuple(int(c) for _ in range(N) for c in counts.split(","))
        count, counts = counts[0], counts[1:]

        print(f"{p+1} out of 1000", end="\r")
        res = dp(record, counts, count, False)
        sum += res
    print()
    return sum

@cache
def dp(record: str, counts: Tuple[int], count: int, started: bool):
    char, record = record[0], record[1:]
    match (char, count):
        case ('#', 0): return 0
        case ('#', _): return (
                0 if len(record) == 0 and count != 1 else
                1 if len(record) == 0 and count == 1 and len(counts) == 0 else
                0 if len(record) == 0 and count == 1 and len(counts) != 0 else
                dp(record, counts, count - 1, True)
        )

        case ('.', 0): return (
            1 if len(counts) == 0 and len(record) == 0 else
            0 if len(counts) >  0 and len(record) == 0 else
            dp(record, counts, count, False) if len(counts) == 0 and len(record) > 0 else
            dp(record, counts[1:], counts[0], False)
        )
        case ('.', _): return (
            0 if started or len(record) == 0 else
            dp(record, counts, count, False)
        )

        case ('?', _): return (
            dp('.'+record, counts, count, started)
          + dp('#'+record, counts, count, started)
        )

def map_replace(S: str, R: str, i: int):
    return S[:i] + R + S[i + 1 :]

if __name__ == "__main__":
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else "d12.in"
    inp = open(infile).read().strip()
    # print(f'A: {partA(inp[::])}')
    print(f"B: {partB(inp[::])}")
