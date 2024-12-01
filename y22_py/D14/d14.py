import argparse

def main(input):
    # COORDINATES ARE FORMATTED AS (X,Y)
    with open(input, 'r') as r:
        rock_paths = [[tuple([int(p) for p in coord.split(',')]) for coord in line.strip().replace(' -> ', ' ').split(' ')] for line in r.readlines()]
    
    resting_sands = []
    floor = 0

    sand_pos = (500, 0)
    moved = True

    for path in rock_paths:
        for rock in path:
            floor = max(floor, rock[1])

    floor += 2

    while True:
        print('{}\r'.format(len(resting_sands)), end='', flush=True)
        sand_pos, moved = simulate_sand(sand_pos, rock_paths, resting_sands, floor)
        if sand_pos == (500, 0):
            resting_sands.append(sand_pos)
            break

        if not moved:
            resting_sands.append(sand_pos)
            sand_pos = (500, 0)

    
    print(len(resting_sands))

def simulate_sand(pos, rocks, sands, floor):
    d = True
    dL = True
    dR = True

    if pos[1]+1 == floor:
        return pos, False

    # Check through all sand units if current sand can't move down, down left, or down right
    for sand in sands:
        # Check if it can't fall down.
        if pos[0] == sand[0] and pos[1]+1 == sand[1]:
            d = False
        
        # Check if it can't fall down left
        if pos[0]-1 == sand[0] and pos[1]+1 == sand[1]:
            dL = False

        # Check if it can't fall down right
        if pos[0]+1 == sand[0] and pos[1]+1 == sand[1]:
            dR = False

    # Early return might make it more efficient
    if not (d or dL or dR):
        return pos, False

    # Check through all rocks if current sand can't move down, down left, or down right
    for rock in rocks:
        for i in range(len(rock)-1):
            a = rock[i]
            b = rock[i+1]

            # Check if it can't fall down.
            if min(a[0], b[0]) <= pos[0] and pos[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= pos[1]+1 and pos[1]+1 <= max(a[1], b[1]):
                d = False
            
            # Check if it can't fall down left.
            if min(a[0], b[0]) <= pos[0]-1 and pos[0]-1 <= max(a[0], b[0]) and min(a[1], b[1]) <= pos[1]+1 and pos[1]+1 <= max(a[1], b[1]):
                dL = False

            # Check if it can't fall down right.
            if min(a[0], b[0]) <= pos[0]+1 and pos[0]+1 <= max(a[0], b[0]) and min(a[1], b[1]) <= pos[1]+1 and pos[1]+1 <= max(a[1], b[1]):
                dR = False

    if d:
        return ((pos[0], pos[1]+1), True)
    if dL:
        return ((pos[0]-1, pos[1]+1), True)
    if dR:
        return ((pos[0]+1, pos[1]+1), True)
    return pos, False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)