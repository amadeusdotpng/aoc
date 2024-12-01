from collections import deque
inp = [line.strip() for line in open(0).readlines()]

R = {}
P = {}

for valve in inp:
    info = valve.split(';')
    R[info[0]] = int(info[1])
    P[info[0]] = tuple(info[2].split(', '))

for valve in R:
    paths = deque(P[valve])
    L = deque()
    explored = set()

    if R[valve] == 0 and valve != 'AA':
        continue
    
    explored.add(paths[0])
    explored.add(valve)
    print(valve,'\n')
    while paths:
        path = paths.popleft()
        print(path, end=' ')
        print(R[path], end='')
        
        if R[path] > 0 and path in explored:
            L.appendleft(path)
            explored.add(path)
            print(' added')
            continue
        
        print(' not added')
        for posPath in P[path]:
            
            if posPath in explored:
                continue
            print(posPath, 'added to explore')
            paths.appendleft(posPath)
            explored.add(posPath)
        

    print()
    P[valve] = tuple(L)
    print(P)



    