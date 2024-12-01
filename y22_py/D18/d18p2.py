import queue

inp = set([tuple(int(x) for x in line.strip().split(',')) for line in open(0).readlines()])
min_x = min(inp, key=lambda n: n[0])[0]
min_y = min(inp, key=lambda n: n[1])[1]
min_z = min(inp, key=lambda n: n[2])[2]
max_x = max(inp, key=lambda n: n[0])[0]
max_y = max(inp, key=lambda n: n[1])[1]
max_z = max(inp, key=lambda n: n[2])[2]

def get_edges(x, y, z):
    return [(x+1, y, z), (x-1, y, z),
            (x, y+1, z), (x, y-1, z),
            (x, y, z+1), (x, y, z-1)]

def flood_fill(start, max):
    face_sum = 0

    # Edge limit
    sX, sY, sZ = start
    mX, mY, mZ = max
    
    # Use something like BFS
    explored = set()
    Q = queue.Queue()
    Q.put(start)
    explored.add(start)
    
    # BFS kinda
    while len(Q.queue) != 0:
        x, y, z = Q.get()

        # Check for each face of current cube if there's a block there
        if (x+1, y, z) in inp:
            face_sum += 1
        if (x-1, y, z) in inp:
            face_sum += 1
        if (x, y+1, z) in inp:
            face_sum += 1
        if (x, y-1, z) in inp:
            face_sum += 1
        if (x, y, z+1) in inp:
            face_sum += 1
        if (x, y, z-1) in inp:
            face_sum += 1

        edge_cubes = get_edges(x, y, z)
        for cube in edge_cubes:
            cX, cY, cZ = cube
            if sX <= cX <= mX and sY <= cY <= mY and sZ <= cZ <= mZ and cube not in (inp | explored):
                Q.put(cube)
                explored.add(cube)
    
    return face_sum

print(flood_fill((min_x-1,min_y-1,min_z-1), (max_x+1, max_y+1, max_z+1)))