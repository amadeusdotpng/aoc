from math import lcm

def partA(input: str):
    instructions, paths = input.split('\n\n')
    pathslist = paths.splitlines()
    
    paths = {}
    for path in pathslist:
        loc, options = path.split(' = ')
        options = options.replace('(', '').replace(')', '').split(', ')
        paths[loc] = options

    steps = 0
    current_location = 'AAA'
    i = 0
    while True:
        direction = instructions[i%len(instructions)]
        if current_location == 'ZZZ':
            return steps
        if direction == 'L':
            current_location = paths[current_location][0]
            steps += 1
            i += 1
            continue
        if direction == 'R':
            current_location = paths[current_location][1]
            steps += 1
            i += 1
            continue

def partB(input: str):
    instructions, paths = input.split('\n\n')
    pathslist = paths.splitlines()
    
    paths = {}
    for path in pathslist:
        loc, options = path.split(' = ')
        options = options.replace('(', '').replace(')', '').split(', ')
        paths[loc] = options

    locations = {}
    for path in paths:
        if path[2] == 'A':
            locations[path] = (path, 0)

    i = 0
    while True:
        direction = instructions[i%len(instructions)]
        for loc in locations:
            curr_loc, steps = locations[loc]
            if curr_loc[2] == 'Z':
                continue

            if direction == 'L':
                locations[loc] = (paths[curr_loc][0], steps+1)

            if direction == 'R':
                locations[loc] = (paths[curr_loc][1], steps+1)
        i += 1

        s = set([x[0][2] for x in locations.values()])
        if len(s) == 1 and 'Z' in s:
            return lcm(*[x[1] for x in locations.values()])

    
            

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd08.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
