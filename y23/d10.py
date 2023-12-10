from queue import Queue
def get_start(map):
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col == 'S':
                return (i, j)
    
def get_edges(map, node):
    row, col = node
#    print(row, col, node, map[row][col])
    if map[row][col] == '|' or map[row][col] == 'S':
        return [(row-1, col), (row+1, col)]
    if map[row][col] == '-':
        return [(row, col-1), (row, col+1)]
    if map[row][col] == 'L':
        return [(row-1, col), (row, col+1)]
    if map[row][col] == 'J':
        return [(row-1, col), (row, col-1)]
    if map[row][col] == '7':
        return [(row, col-1), (row+1, col)]
    if map[row][col] == 'F':
        return [(row, col+1), (row+1, col)]

def partA(input: str):
    map = [[c for c in line] for line in input.splitlines()]
    Q = Queue() 
    root = get_start(map)
    steps = {root: 0}
    explored = set([root])
    Q.put(root)
    while not Q.empty():
        node = Q.get()
        for edge in get_edges(map, node):
            if edge in explored:
                continue
            if not (0 <= edge[0] <= len(map)-1 and 0 <= edge[1] <= len(map[0])-1):
                continue
            Q.put(edge)
            explored.add(edge)
            steps[edge] = steps[node]+1
    return max(steps.values())

def partB(input: str):
    map = [[c for c in line] for line in input.splitlines()]
    # Get tiles that are part of the loop
    Q = Queue() 
    root = get_start(map)
    explored = set([root])
    Q.put(root)
    while not Q.empty():
        node = Q.get()
        for edge in get_edges(map, node):
            if edge in explored:
                continue
            if not (0 <= edge[0] <= len(map)-1 and 0 <= edge[1] <= len(map[0])-1):
                continue
            Q.put(edge)
            explored.add(edge)
    
    # Test each tile if it's in the loop by counting the number of intersections when going right, down
    # Both tests must be the same or else something must have gone wrong.
    # If the number of intersections are even, it's outside of the loop
    # If the number of intersections are odd, it's inside of the loop
    tiles = set()
    for row in range(len(map)):
        for col in range(len(map[row])):
            if (row,col) in explored:
                continue
            r = d = 0
            corners = {'F': False, 'J': False, 'L': False, '7': False}
            # col+1 to end
            for x in range(col+1, len(map[row])):
                if (row, x) not in explored:
                    continue
                tile = map[row][x]
                if tile == 'F' and (corners['J'] or corners['L']):
                    continue
                if tile == 'J' and (corners['F'] or corners['7']):
                    continue
                if tile == 'L' and (corners['7'] or corners['F']):
                    continue
                if tile == '7' and (corners['L'] or corners['J']):
                    continue
                if tile == '-':
                    continue
                if tile == 'F': corners = {'F': True, 'J': False, 'L': False, '7': False}
                if tile == 'J': corners = {'F': False,'J': True,  'L': False, '7': False}
                if tile == 'L': corners = {'F': False,'J': False, 'L': True,  '7': False}
                if tile == '7': corners = {'F': False,'J': False, 'L': False, '7': True}
                r += 1

            corners = {'F': False, 'J': False, 'L': False, '7': False}
            # row+1 to end
            for y in range(row+1, len(map)):
                if (y, col) not in explored:
                    continue
                tile = map[y][col]
                if tile == 'F' and (corners['J'] or corners['7']):
                    continue
                if tile == 'J' and (corners['F'] or corners['L']):
                    continue
                if tile == 'L' and (corners['7'] or corners['J']):
                    continue
                if tile == '7' and (corners['L'] or corners['F']):
                    continue
                if tile == '|' or tile == 'S':
                    continue
                if tile == 'F' and (y, col) in explored: corners = {'F': True, 'J': False, 'L': False, '7': False}
                if tile == 'J' and (y, col) in explored: corners = {'F': False,'J': True,  'L': False, '7': False}
                if tile == 'L' and (y, col) in explored: corners = {'F': False,'J': False, 'L': True,  '7': False}
                if tile == '7' and (y, col) in explored: corners = {'F': False,'J': False, 'L': False, '7': True}
                d += 1
            r %= 2
            d %= 2
            assert r == d
            if r and (row, col) not in explored:
                tiles.add((row, col))
    return len(tiles)

            
if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd10.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
