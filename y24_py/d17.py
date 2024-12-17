from collections import deque


def run_program(reg, program):
    inst_pointer = 0
    out = []
    while inst_pointer < len(program):
        opcode = program[inst_pointer]
        opinpt = program[inst_pointer+1]
        assert opinpt != 7
        combo = reg.get(opinpt, opinpt)
        liter = opinpt

        if opcode == 0:
            reg[4] = reg[4] >> combo

        elif opcode == 1:
            reg[5] = reg[5] ^ liter

        elif opcode == 2:
            reg[5] = combo % 8

        elif opcode == 3:
            if reg[4] != 0:
                inst_pointer = liter
                continue
        elif opcode == 4:
            reg[5] = reg[5] ^ reg[6]

        elif opcode == 5:
            out.append(combo % 8)

        elif opcode == 6:
            reg[5] = reg[4] >> combo

        elif opcode == 7:
            reg[6] = reg[4] >> combo

        inst_pointer += 2

    return out

def partA(inp: str):
    reg, program = inp.split('\n\n')
    reg = {idx+4: int(r[12:]) for idx, r in enumerate(reg.splitlines())}
    program = list(map(int, program[9:].split(',')))

    out = run_program(reg, program)
    return ','.join(str(n) for n in out)

def partB(inp: str):
    _, program = inp.split('\n\n')
    program = list(map(int, program[9:].split(',')))

    Q = deque([(n, 1) for n in range(2**10)])

    #print(''.join(str(k) for k in program))
    while Q:
        n, idx = Q.popleft()
        m = program[:idx]

        reg = {4: n, 5: 0, 6: 0}
        res = run_program(reg, program)

        #print(''.join(str(res[i]) if i < len(res) else 'X' for i in range(16)), f'{n:0>20}', idx, end='\r')

        if res[:idx] != m:
            continue

        if res == program:
            #print(''.join(str(res[i]) if i < len(res) else 'X' for i in range(16)), f'{n:0>20}', idx, end='\r')
            #print()
            return n

        if idx+1 >= len(program):
            continue


        for k in range(1,2**4):
            e = n | k << n.bit_length()
            '''
            print(f'{k:0>3b} {n:b}')
            print(f'{e:b}')
            print()
            '''
            Q.append((e, idx+1))

def partC(inp: str):
    _, program = inp.split('\n\n')
    program = list(map(int, program[9:].split(',')))

    reg = {4: 0, 5: 0, 6: 0}
    [rest] = run_program(reg, program)

    # from time import sleep
    # print(''.join(str(k) for k in program))
    Q = deque([(n, rest) for n in range(8)])
    while Q:
        n, rest = Q.popleft()
        m = n | (rest << 3)
        reg = {4: m, 5: 0, 6: 0}

        res = run_program(reg, program)

        # print(f'{''.join(str(s) for s in res):X>{len(program)}}', f'{m:0>15}', end='\r')
        # sleep(0.050)

        if res != program[-len(res):]:
            continue

        if res == program:
            # print()
            return m

        if len(res) > len(program):
            continue

        for k in range(8):
            Q.append((k, m))

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd17.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partC(inp[::])}')
