DIRS = [-1+0j, 0+1j, 1+0j, 0-1j]

def get_tiles(pos, dir, obstacles, W, H):
    in_bounds = lambda p: 0 <= p.real <= H-1 and 0 <= p.imag <= W-1
    path = set()
    while in_bounds(pos) :
        path.add(pos)
        if pos + DIRS[dir] in obstacles:
            dir = (dir + 1) % 4
        else:
            pos += DIRS[dir]
    return path

def partA(inp: str):
    pos = None
    obstacles = set()
    inp = [line.strip() for line in inp.splitlines()]
    W, H = len(inp), len(inp[0])
    for row, line in enumerate(inp):
        for col, char in enumerate(line):
            if char == '#': obstacles.add(complex(row, col))
            if char == '^': pos = complex(row, col)

    return len(get_tiles(pos, 0, obstacles, W, H))

# SOLUTIONS:
# (6, 3)
# (7, 6)
# (7, 7)
# (8, 1)
# (8, 3)
# (9, 7)

def partB(inp: str):
    pos = None
    dir = 0
    obstacles = set()
    inp = [line.strip() for line in inp.splitlines()]
    W, H = len(inp), len(inp[0])
    for row, line in enumerate(inp):
        for col, char in enumerate(line):
            if char == '#': obstacles.add(complex(row, col))
            if char == '^': pos = complex(row, col)

    in_bounds = lambda p: 0 <= p.real <= H-1 and 0 <= p.imag <= W-1
    S = 0
    visited = get_tiles(pos, 0, obstacles, W, H)
    for tile in visited:
        new_obstacles = obstacles.union({tile})
        new_pos = pos
        new_dir = dir

        path = set()

        # Now we will travel the path with this new obstacle
        while 0 <= new_pos.imag <= W-1 and 0 <= new_pos.real <= H-1:

            if (new_pos, DIRS[new_dir]) in path:
                # If we have, the obstruction we are testing creates a loop, no need to go further
                S += 1
                break

            # If not, add it to the temporary visited set
            path.add((new_pos, DIRS[new_dir]))

            # Move or turn like we did in part 1
            if new_pos + DIRS[new_dir] in new_obstacles:
                new_dir = (new_dir + 1) % 4
            else:
                new_pos += DIRS[new_dir]
            '''
            ahead = new_pos + DIRS[new_dir]
            if ahead in new_obstacles:
                new_dir = (new_dir + 1) % 4
                ahead = new_pos + DIRS[new_dir]

            new_pos = ahead
            '''
    return S

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd06.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
