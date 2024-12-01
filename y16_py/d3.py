def partA(input: str):
    input = [[int(n) for n in line.split()] for line in input.splitlines()]
    count = 0
    for tri in input:
        tri.sort()
        if tri[0] + tri[1] > tri[2]:
            count += 1
    return count


def partB(input: str):
    input = [[int(n) for n in line.split()] for line in input.splitlines()]
    count = 0
    for j in range(0, len(input), 3):
        for i in range(3):
            tri = [input[j][i], input[j+1][i], input[j+2][i]]
            tri.sort()
            if tri[0] + tri[1] > tri[2]:
                count += 1
    return count

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd0.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
