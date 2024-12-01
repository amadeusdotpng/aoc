import argparse


def main(input):
    with open(input, 'r') as r:
        grid = r.readlines()
        grid = [[int(x) for x in l.strip()] for l in grid]
        # print(grid)
        scores = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                cell = grid[y][x]
                coord = (y,x)
                scores.append(getUp(grid, coord) * getDown(grid, coord) * getLeft(grid, coord) * getRight(grid, coord))
        print(max(scores))
        
def getUp(grid, coord):
    y_ = coord[0]
    x_ = coord[1]
    cell = grid[y_][x_]
    score = 0

    for y in range(y_, -1, -1):
        if y == y_:
            continue

        score += 1

        if cell <= grid[y][x_]:
            break
        
    return score
            
def getDown(grid, coord):
    y_ = coord[0]
    x_ = coord[1]
    cell = grid[y_][x_]
    score = 0

    for y in range(y_, len(grid)):
        if y == y_:
            continue

        score += 1

        if cell <= grid[y][x_]:
            break
        
    return score

def getLeft(grid, coord):
    y_ = coord[0]
    x_ = coord[1]
    cell = grid[y_][x_]
    score = 0

    for x in range(x_, -1, -1):
        if x == x_:
            continue

        score += 1

        if cell <= grid[y_][x]:
            break
        
    return score

def getRight(grid, coord):
    y_ = coord[0]
    x_ = coord[1]
    cell = grid[y_][x_]
    score = 0

    for x in range(x_, len(grid[y_])):
        if x == x_:
            continue

        score += 1

        if cell <= grid[y_][x]:
            break
        
    return score
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)