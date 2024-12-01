def partA(input: str):
    input = input.splitlines()
    time = [int(x) for x in input[0].split()[1:]]
    record = [int(x) for x in input[1].split()[1:]]
    count = 1
    for i, t in enumerate(time):
        ways = 0
        for n in range(t):
            dt = (t-n)*n
            if dt > record[i]:
                ways += 1
        count *= ways
    return count

def partB(input: str):
    input = input.splitlines()
    time = [int(''.join(input[0].split()[1:]))]
    record = [int(''.join(input[1].split()[1:]))]
    count = 1
    for i, t in enumerate(time):
        ways = 0
        for n in range(t):
            dt = (t-n)*n
            if dt > record[i]:
                ways += 1
        count *= ways
    return count

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd6.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
    print()
