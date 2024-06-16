inp = [tuple(int(x) for x in line.strip().split(',')) for line in open(0).readlines()]
cubes = {}
# print(inp)
for line in inp:
    exposed_face = 6
    # Check for every face and see if thsoe coordinates are in the set
    x, y, z = line
    if (x+1, y, z) in inp:
        exposed_face -= 1
    if (x-1, y, z) in inp:
        exposed_face -= 1
    if (x, y+1, z) in inp:
        exposed_face -= 1
    if (x, y-1, z) in inp:
        exposed_face -= 1
    if (x, y, z+1) in inp:
        exposed_face -= 1
    if (x, y, z-1) in inp:
        exposed_face -= 1
    cubes[(x,y,z)] = exposed_face
sum = 0
for cube in cubes:
    sum += cubes[cube]

print(sum)
