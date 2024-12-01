import argparse

def main(input):
    with open(input, 'r') as r:
        grid = r.readlines()
        grid = [[int(x) for x in l.strip()] for l in grid]
        # print(grid)
        visible_coords = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                cell = grid[y][x]
                
                # If they are on the edge
                if y == 0 or y == len(grid)-1 or x == 0 or x == len(grid[y])-1:
                    visible_coords.append((y,x))
                    continue

                # Check for left and right, then up or down
                visible = visibleUp(grid, (y,x)) or visibleDown(grid, (y,x)) or visibleLeft(grid, (y,x)) or visibleRight(grid, (y,x))
                # visible = visibleRight(grid, (y,x))
                if visible:
                    visible_coords.append((y,x))
                    continue

        for y, x in visible_coords:
            grid[y][x] = 0
        
        print(grid)
        print(len(visible_coords))
                
        
def visibleUp(grid, coord):
    y_ = coord[0]
    x_ = coord[1]
    cell = grid[y_][x_]
    cells = []

    for y in range(0, y_):
        if y != y_:
            cells.append(grid[y][x_])

    if max(cells) < cell:
        return True
    return False

def visibleDown(grid, coord):
    y_ = coord[0]
    x_ = coord[1]
    cell = grid[y_][x_]
    cells = []

    for y in range(y_, len(grid)):
        if y != y_:
            cells.append(grid[y][x_])

    if max(cells) < cell:
        return True
    return False

def visibleLeft(grid, coord):
    y_ = coord[0]
    x_ = coord[1]
    cell = grid[y_][x_]
    cells = []

    for x in range(0, x_):
        if x != x_:
            cells.append(grid[y_][x])

    if max(cells) < cell:
        return True
    return False

def visibleRight(grid, coord):
    y_ = coord[0]
    x_ = coord[1]
    cell = grid[y_][x_]
    cells = []

    for x in range(x_, len(grid[y_])):
        if x != x_:
            cells.append(grid[y_][x])

    if max(cells) < cell:
        return True
    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)