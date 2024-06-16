
input = open(0)
impossible_coords = set()
beacon_x = set()
row = 2000000
def manhattan_dist(s, b):
    return abs(b[0]-s[0]) + abs(b[1]-s[1])

for line in input:
    sensor, beacon = ([int(x) for x in pair.split(', ')] for pair in line.strip().split(':'))
    if beacon[1] == row:
        beacon_x.add(beacon[0])
    total_dist = manhattan_dist(sensor, beacon)
    dist_to_row = abs(row - sensor[1])
    distance_left = total_dist-dist_to_row
    if distance_left > 0:
        for i in range(-distance_left, distance_left+1):
            x_coord = sensor[0]+i
            impossible_coords.add(x_coord)

print(len(impossible_coords ^ (impossible_coords & beacon_x)))
    

