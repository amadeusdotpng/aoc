import argparse
import numpy as np
import cv2
def main(input):

    # Grid Setup
    with open(input, 'r') as r:
        rock_paths = [[tuple([int(p) for p in coord.split(',')]) for coord in line.strip().replace(' -> ', ' ').split(' ')] for line in r.readlines()]
    minx = rock_paths[0][0][0]
    wd = 0
    ht = 0

    
    for path in rock_paths:
        for rock in path:
            minx = min(rock[0], minx)
            wd = max(rock[0], wd)
            ht = max(rock[1], ht)
    ht += 3
    gridmap = np.full((ht, wd-minx+1000), 0, dtype=np.uint8)
    minx = minx//2
    for path in rock_paths:
        for i in range(len(path)):
            path[i] = (path[i][0]-minx, path[i][1])

    for path in rock_paths:
        for i in range(len(path)-1):
            a = path[i]
            b = path[i+1]
            generate_wall(gridmap, a, b)

        # Create Floor
    for i in range(len(gridmap[ht-1])):
        gridmap[ht-1][i] = 255

    

    # Simulation
    sand_pos = (500-minx,0)
    resting_sands = []
    while True:
        print('{}\r'.format(len(resting_sands)), end='', flush=True)
        sand_pos, moved = simulate_sand(gridmap, sand_pos)
        if sand_pos == (500-minx, 0):
            gridmap[sand_pos[1]][sand_pos[0]] = 125
            resting_sands.append(sand_pos)
            break

        if not moved:
            gridmap[sand_pos[1]][sand_pos[0]] = 125
            resting_sands.append(sand_pos)
            sand_pos = (500-minx, 0)

        if len(resting_sands) > 40000:
            break
    cv2.imshow('map', cv2.resize(gridmap, (0,0), fx=3, fy=3, interpolation=cv2.INTER_AREA))
    cv2.waitKey()
        


def generate_wall(grid, a, b):
    # Horizontal Wall
    if abs(a[0]-b[0]) > 0:
        for i in range(min(a[0], b[0]), max(a[0], b[0])+1):
            grid[a[1]][i] = 255
    # Vertical Wall
    else:
        for i in range(min(a[1], b[1]), max(a[1], b[1])+1):
            grid[i][a[0]] = 255

def simulate_sand(grid, pos):
    col = pos[0]
    row = pos[1]
    
    # Check if it hit floor
    if row+1 >= len(grid)-1:
        return pos, False

    # Check if it can move down
    if grid[row+1][col] == 0:
        return ((col, row+1), True)

    # Check if it can move down left
    if grid[row+1][col-1] == 0:
        return ((col-1, row+1), True)

    # Check if it can move down right
    if grid[row+1][col+1] == 0:
        return ((col+1, row+1), True)
    return pos, False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)