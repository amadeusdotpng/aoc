def check_area(num_coord, symbol_coords):
    for y in range(num_coord[2]-1, num_coord[2]+2):
        for x in range(num_coord[0]-1, num_coord[1]+2):
            coord = (x, y)
            if not (0 <= x <= 139 and 0 <= y <= 139):
                continue
            if coord in symbol_coords:
                return True
    return False

def partA(input: str):
    input = input.splitlines()
    symbol_coords = set()
    sum = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            symbol = input[y][x]
            if symbol != '.' and not symbol.isdigit():
                symbol_coords.add((x, y))

    num_coords = {}
    for y, line in enumerate(input):
        start = end = None
        num = ""
        for x, c in enumerate(line):
            if c.isdigit() and start is None:
                start = x
                num += c
                continue
            if c.isdigit() and start is not None:
                num += c
                continue
            if not c.isdigit() and start is not None and end is None:
                end = x-1
                num_coords[(start, end, y)] = int(num)
                start = end = None
                num = ""
        if start is not None:
            end = x-1
            num_coords[(start, end, y)] = int(num)
            start = end = None
            num = ""

    for coord in num_coords:
        if check_area(coord, symbol_coords):
            sum += num_coords[coord]
    return sum

def check_gear(num_coord, symbol_coords, used_gears):
    for y in range(num_coord[2]-1, num_coord[2]+2):
        for x in range(num_coord[0]-1, num_coord[1]+2):
            coord = (x, y)
            if not (0 <= x <= 139 and 0 <= y <= 139):
                continue
            if coord in symbol_coords and not (coord in used_gears):
                return coord
    return None

def partB(input: str):
    input = input.splitlines()
    gear_coords = set()
    sum = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            symbol = input[y][x]
            if symbol == '*' and not symbol.isdigit():
                gear_coords.add((x, y))

    num_coords = {}
    for y, line in enumerate(input):
        start = end = None
        num = ""
        for x, c in enumerate(line):
            if c.isdigit() and start is None:
                start = x
                num += c
                continue
            if c.isdigit() and start is not None:
                num += c
                continue
            if not c.isdigit() and start is not None and end is None:
                end = x-1
                num_coords[(start, end, y)] = int(num)
                start = end = None
                num = ""
        if start is not None:
            end = x-1
            num_coords[(start, end, y)] = int(num)
            start = end = None
            num = ""

    used_gears = set()
    for coordA in num_coords:
        gear_coordA = check_gear(coordA, gear_coords, used_gears)
        if not gear_coordA:
            continue
        for coordB in num_coords:
            gear_coordB = check_gear(coordB, gear_coords, used_gears)
            if coordA != coordB and gear_coordA == gear_coordB:
                used_gears.add(gear_coordA)
                sum += num_coords[coordA] * num_coords[coordB]
                break
    return sum

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd3.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
