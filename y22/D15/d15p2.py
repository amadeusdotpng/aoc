
input = open(0)

M = 4_000_000


input = [[[int(x) for x in pair.split(', ')] for pair in line.strip().split(':')] for line in input]

def manhattan_dist(s, b):
    return abs(b[0]-s[0]) + abs(b[1]-s[1])

for row in range(0, M+1):
    intervals = []
    if row % 100 == 0:
        print(row, end='\r')
    for line in input:
        sensor, beacon = line
        total_dist = manhattan_dist(sensor, beacon)
        dt_left = total_dist - abs(sensor[1]-row)
        
        if dt_left < 0:
            continue

        lx = sensor[0]-dt_left
        hx = sensor[0]+dt_left
        intervals.append([lx, hx])
    
    intervals.sort()
    full_interval = []

    for interval in intervals:
        if not full_interval:
            full_interval.append(interval)
            continue

        full = full_interval[-1]

        if interval[0] <= full[1]+1:
            full[1] = max(full[1], interval[1])
        else:
            full_interval.append(interval)
    
    if not (full_interval[0][0] <= 0 and full_interval[0][1]) >= M:
        print(row)
        print(full_interval[0][1]+1)
        exit(0)