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

        match opcode:
            case 0: reg[4] = reg[4] >> combo
            case 1: reg[5] = reg[5] ^ liter
            case 2: reg[5] = combo % 8

            case 3 if reg[4] != 0: 
                inst_pointer = liter
                continue

            case 4: reg[5] = reg[5] ^ reg[6]
            case 5: out.append(combo % 8)
            case 6: reg[5] = reg[4] >> combo
            case 7: reg[6] = reg[4] >> combo

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

    Q = deque([(n, 0) for n in range(8)])
    while Q:
        n, rest = Q.popleft()
        m = n | (rest << 3)
        reg = {4: m, 5: 0, 6: 0}

        res = run_program(reg, program)

        if res != program[-len(res):]:
            continue

        if res == program:
            return m

        for k in range(8):
            Q.append((k, m))

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd17.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
