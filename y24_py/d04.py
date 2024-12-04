def transpose(inp):
    return list(map(lambda x: ''.join(c for c in x), zip(*inp)))

def partA(inp: str):
    S = 0
    inp = [line for line in inp.splitlines()]

    t_inp = transpose(inp)
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            c = inp[row][col]

            if c != 'X':
                continue

            # check forward + backward
            S += inp[row][col:col+4] == 'XMAS'
            S += inp[row][col-3:col+1] == 'SAMX'

            # check up + down
            S += t_inp[col][row:row+4] == 'XMAS'
            S += t_inp[col][row-3:row+1] == 'SAMX'

            # check top-left to bottom-right:
            if row <= len(inp)-4 and col <= len(inp[row])-4:
                S += ''.join(inp[row+i][col+i] for i in range(4)) == 'XMAS'

            # check bottom-right to top-left
            if row >= 3 and col >= 3:
                S += ''.join(inp[row-i][col-i] for i in range(4)) == 'XMAS'

            # check top-right to bottom-left:
            if row <= len(inp)-4 and col >= 3:
                S += ''.join(inp[row+i][col-i] for i in range(4)) == 'XMAS'

            # check bottom-left to top-right
            if row >= 3 and col <= len(inp[row])-4:
                S += ''.join(inp[row-i][col+i] for i in range(4)) == 'XMAS'

    return S

def partB(inp: str):
    S = 0
    inp = [[c for c in line] for line in inp.splitlines()]
    for row in range(len(inp)-2):
        for col in range(len(inp[row])-2):
            block = [inp[row+i][col:col+3] for i in range(3)]


            S += (
                block[1][1] == 'A' and (
                (block[0][0] == 'M' and block[2][2] == 'S' and block[2][0] == 'M' and block[0][2] == 'S') or
                (block[0][0] == 'S' and block[2][2] == 'M' and block[2][0] == 'M' and block[0][2] == 'S') or
                (block[0][0] == 'M' and block[2][2] == 'S' and block[2][0] == 'S' and block[0][2] == 'M') or
                (block[0][0] == 'S' and block[2][2] == 'M' and block[2][0] == 'S' and block[0][2] == 'M')
                )
            )
            
    return S

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd04.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
