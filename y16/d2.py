def partA(input: str):
    input = input.splitlines()
    nums = ["123", "456", "789"]
    password = ""
    index = 0+0j
    for combination in input:
        for direction in combination:
            match direction:
                case 'U':
                    new_index = index-1j
                    index = new_index if 0 <= new_index.imag <= 2 else index
                case 'D':
                    new_index = index+1j
                    index = new_index if 0 <= new_index.imag <= 2 else index
                case 'R':
                    new_index = index+1
                    index = new_index if 0 <= new_index.real <= 2 else index
                case 'L':
                    new_index = index-1
                    index = new_index if 0 <= new_index.real <= 2 else index
        password += nums[int(index.imag)][int(index.real)]
    return password
            

def partB(input: str):
    input = input.splitlines()
    nums = ["00100", "02340", "56789", "0ABC0", "00D00"]
    password = ""
    index = 0+2j
    for combination in input:
        for direction in combination:
            match direction:
                case 'U':
                    new_index = index-1j
                    if 0 <= new_index.imag <= 4:
                        index = new_index if nums[int(new_index.imag)][int(new_index.real)] != "0" else index
                case 'D':
                    new_index = index+1j
                    if 0 <= new_index.imag <= 4:
                        index = new_index if nums[int(new_index.imag)][int(new_index.real)] != "0" else index
                case 'R':
                    new_index = index+1
                    if 0 <= new_index.real <= 4:
                        index = new_index if nums[int(new_index.imag)][int(new_index.real)] != "0" else index
                case 'L':
                    new_index = index-1
                    if 0 <= new_index.real <= 4:
                        index = new_index if nums[int(new_index.imag)][int(new_index.real)] != "0" else index
        password += nums[int(index.imag)][int(index.real)]
    return password

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd0.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
