import argparse

def main(input):
    with open(input, 'r') as r:
        instructions = [line.split(' ') for line in r.readlines()]

        # (X,Y)
        body = [(0,0) for i in range(10)]
        
        tail_trail = set()
        for inst, n in instructions:
            # print(inst, n)
            for i in range(int(n)):
                tail_trail.add(body[9])
                move_head(body, inst)
                tail_trail.add(body[9])
                # print(body)
                # print(body)
                
                
        print(len(tail_trail))
        # print(tail_trail)
        # print(body)


def move_head(body, move):
    if   move == 'U':
        body[0] = (body[0][0], body[0][1]+1)
    elif move == 'D':
        body[0] = (body[0][0], body[0][1]-1)
    elif move == 'L':
        body[0] = (body[0][0]-1, body[0][1])
    elif move == 'R':
        body[0] = (body[0][0]+1, body[0][1])
    
    for i in range(1, len(body)):    
        body[i] = fix_tail(body[i-1], body[i])
        # print(i, body[i-1], body[i])
       
    
    # print('')

def fix_tail(head, tail):
    if head[1] - tail[1] > 1 and head[0] == tail[0]:    # SHOULD GO UP
        return (tail[0], tail[1]+1)

    if head[1] - tail[1] < -1 and head[0] == tail[0]:   # SHOULD GO DOWN
        return (tail[0], tail[1]-1)
        
    if head[0] - tail[0] < -1 and head[1] == tail[1]:   # SHOULD GO LEFT
        return (tail[0]-1, tail[1])
    
    if head[0] - tail[0] > 1 and head[1] == tail[1]:    # SHOULD GO RIGHT
        return (tail[0]+1, tail[1])
    
    if (head[0] == tail[0]+1 and head[1] == tail[1]+2) or (head[0] == tail[0]+2 and head[1] == tail[1]+1) or (head[0] == tail[0]+2 and head[1] == tail[1]+2):
        return (tail[0]+1, tail[1]+1)
    
    if (head[0] == tail[0]-1 and head[1] == tail[1]+2) or (head[0] == tail[0]-2 and head[1] == tail[1]+1) or (head[0] == tail[0]-2 and head[1] == tail[1]+2):
        return (tail[0]-1, tail[1]+1)

    if (head[0] == tail[0]-1 and head[1] == tail[1]-2) or (head[0] == tail[0]-2 and head[1] == tail[1]-1) or (head[0] == tail[0]-2 and head[1] == tail[1]-2):
        return (tail[0]-1, tail[1]-1)

    if (head[0] == tail[0]+1 and head[1] == tail[1]-2) or (head[0] == tail[0]+2 and head[1] == tail[1]-1) or (head[0] == tail[0]+2 and head[1] == tail[1]-2):
        return (tail[0]+1, tail[1]-1)
    
    return tail
    
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)