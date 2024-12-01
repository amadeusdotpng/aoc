import argparse
import queue

def main(input):
    with open(input, 'r') as r:

        grid = [[c for c in line.strip()] for line in r.readlines()]
        start_coords = []
        end_coord = (0,0)
        
        paths = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 'S':
                    grid[y][x] = 'a'
                    # start_coord = (y,x)
                if grid[y][x] == 'E':
                    grid[y][x] = 'z'
                    end_coord = (y,x)
                if grid[y][x] == 'a':
                    start_coords.append((y,x))

        for start in start_coords:
            paths.append(BFS(grid, start, end_coord))

        non_empty_paths = []
        for path in paths:
            if len(path) != 0:
                non_empty_paths.append(len(path))
        
        print(min(non_empty_paths)-1)

def BFS(grid, start, end):
    path = []
    parents = {}
    explored = set()
    search = queue.Queue()

    explored.add(start)
    search.put(start)

    while not search.empty():
        current_coord = search.get()
        current_edges = get_edges(grid, current_coord)
        
        if current_coord == end:
            break

        for edge in current_edges:
            if edge not in explored:
                explored.add(edge)
                parents[edge] = current_coord
                search.put(edge)
    if current_coord != end:
        return []
    path.append(current_coord)
    while True:
        if current_coord not in parents:
            break

        current_coord = parents[current_coord]
        path.append(current_coord)
    return path[::-1]
    
def get_edges(grid, coord):
    edges = []
    y = coord[0]
    x = coord[1]
    # print('y:',y, y-1, y+1, len(grid))
    # print('x:',x, x-1, x+1, len(grid[y]))
    # print('')

    if y < len(grid)-1:
        if ord(grid[y+1][x])-1 <= ord(grid[y][x]):
            edges.append((y+1,x))

    if y > 0:
        if ord(grid[y-1][x])-1 <= ord(grid[y][x]):
            edges.append((y-1,x))

    if x > 0:
        if ord(grid[y][x-1])-1 <= ord(grid[y][x]):
            edges.append((y,x-1))

    if x < len(grid[y])-1:
        if ord(grid[y][x+1])-1 <= ord(grid[y][x]):
            edges.append((y,x+1))

    # print('edges', edges)
    return edges

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)