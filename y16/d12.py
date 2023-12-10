def is_number(n: str):
    try:
        n = int(n)
        return n
    except:
        return None

def do_instructions(input:str, registers: dict):
    input = input.splitlines()
    i = 0
    while i < len(input):
        line = input[i].split()
        instruction, args = line[0], line[1:]
        if instruction == 'cpy':
            val = is_number(args[0]) or registers.get(args[0], 0)
            registers[args[1]] = val
        elif instruction == 'inc':
            val = registers.get(args[0], 0) + 1
            registers[args[0]] = val
        elif instruction == 'dec':
            val = registers.get(args[0], 0) - 1
            registers[args[0]] = val
        elif instruction == 'jnz':
            val = is_number(args[0]) or registers.get(args[0], 0)
            if val != 0:
                i += int(args[1]) # + 1*sign(int(args[1]))
                continue
        i += 1
    return registers['a']
    

def partA(input: str):
    return do_instructions(input, {})

def partB(input: str):
    return do_instructions(input, {'c': 1})

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd12.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
