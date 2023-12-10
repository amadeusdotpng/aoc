SCREEN_WIDTH=50
SCREEN_HEIGHT=6

def partA(input: str):
    input = input.splitlines()
    screen = ['.'*SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]

    for line in input:
        instructions = line.split()
        if instructions[0] == 'rect':
            wd, ht = instructions[1].split('x')
            wd, ht = int(wd), int(ht)

            for row in range(ht):
                screen[row] = '#'*wd+screen[row][wd:]

        elif instructions[0] == 'rotate':
            if instructions[1] == 'row':
                row, qty = int(instructions[2]), (SCREEN_WIDTH-int(instructions[4]))%SCREEN_WIDTH
                screen[row] = screen[row][qty:]+screen[row][:qty]

            elif instructions[1] == 'column':
                col, qty = int(instructions[2]), (SCREEN_HEIGHT-int(instructions[4]))%SCREEN_HEIGHT
                out = ""
                for i in range(SCREEN_HEIGHT):
                    out += screen[i][col]

                out = out[qty:]+out[:qty]

                for i in range(SCREEN_HEIGHT):
                    screen[i] = screen[i][:col]+out[i]+screen[i][col+1:]

    count = 0
    for row in screen:
        for pixel in row:
            if pixel == '#':
                count += 1
    return count


                


def partB(input: str):
    input = input.splitlines()
    screen = ['.'*SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]

    for line in input:
        instructions = line.split()
        if instructions[0] == 'rect':
            wd, ht = instructions[1].split('x')
            wd, ht = int(wd), int(ht)

            for row in range(ht):
                screen[row] = '#'*wd+screen[row][wd:]

        elif instructions[0] == 'rotate':
            if instructions[1] == 'row':
                row, qty = int(instructions[2]), (SCREEN_WIDTH-int(instructions[4]))%SCREEN_WIDTH
                screen[row] = screen[row][qty:]+screen[row][:qty]

            elif instructions[1] == 'column':
                col, qty = int(instructions[2]), (SCREEN_HEIGHT-int(instructions[4]))%SCREEN_HEIGHT
                out = ""
                for i in range(SCREEN_HEIGHT):
                    out += screen[i][col]

                out = out[qty:]+out[:qty]

                for i in range(SCREEN_HEIGHT):
                    screen[i] = screen[i][:col]+out[i]+screen[i][col+1:]

    for row in screen:
        for i in range(len(row)):
            print(row[i], end='')
            if i%5 == 4:
                print(' ', end='')
        print()
    return 'UPOJFLBCEZ'

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd8.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
