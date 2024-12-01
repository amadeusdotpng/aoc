def partA(input: str):
    input = input.splitlines()
    count = 0
    for game_id, line in enumerate(input):
        game_id += 1
        sets = line.split(':')[1].strip().split(';')
        hands = [[cube.split() for cube in hand.split(',')] for hand in sets]
        # rgb
        cubes_seen = [0,0,0]
        for hand in hands:
            for cube in hand:
                if cube[1] == 'red':
                    cubes_seen[0] = max(int(cube[0]), cubes_seen[0])
                if cube[1] == 'green':
                    cubes_seen[1] = max(int(cube[0]), cubes_seen[1])
                if cube[1] == 'blue':
                    cubes_seen[2] = max(int(cube[0]), cubes_seen[2])
        if cubes_seen[0] > 12 or cubes_seen[1] > 13 or cubes_seen[2] > 14:
            continue
        count += game_id
    return count

def partB(input: str):
    input = input.splitlines()
    sum = 0
    for game_id, line in enumerate(input):
        game_id += 1
        sets = line.split(':')[1].strip().split(';')
        hands = [[cube.split() for cube in hand.split(',')] for hand in sets]
        # rgb
        cubes_seen = [0,0,0]
        for hand in hands:
            for cube in hand:
                if cube[1] == 'red':
                    cubes_seen[0] = max(int(cube[0]), cubes_seen[0])
                if cube[1] == 'green':
                    cubes_seen[1] = max(int(cube[0]), cubes_seen[1])
                if cube[1] == 'blue':
                    cubes_seen[2] = max(int(cube[0]), cubes_seen[2])
        sum += cubes_seen[0] * cubes_seen[1] * cubes_seen[2]
    return sum
    

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd2.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
