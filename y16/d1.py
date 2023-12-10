def partA(input: str):
    coord = 0
    direction = [1j, 1, -1j, -1]
    direction_index = 0
    for move in input.split(', '):
        rotate, distance = move[0], int(move[1:])
        if rotate == "R":
            direction_index = (direction_index + 1) % 4
        else:
            direction_index = (direction_index - 1) % 4

        coord += distance*direction[direction_index]

    return int(abs(coord.real)+abs(coord.imag))


def partB(input: str):
    coord = 0
    direction = [1j, 1, -1j, -1]
    direction_index = 0
    visited = set()
    for move in input.split(', '):
        rotate, distance = move[0], int(move[1:])
        if rotate == "R":
            direction_index = (direction_index + 1) % 4
        else:
            direction_index = (direction_index - 1) % 4

        for _ in range(distance):
            coord += direction[direction_index]

            if coord in visited:
                return int(abs(coord.real)+abs(coord.imag))

            visited.add(coord)


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd0.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
