import argparse

def main(stacks_, instructions_):
    with open(stacks_, 'r') as r:
        stacks = [i.strip() for i in r.readlines()]
    
    with open(instructions_, 'r') as r:
        instructions = [[int(i) for i in x.strip().split('.')] for x in r.readlines()]

    for move in instructions:
        # Get n amount of letters from stack
        moving_stack_len = len(stacks[move[1]-1])
        moving_stack = stacks[move[1]-1][moving_stack_len-move[0]:]

        # Set "from stack" to without moving_stack
        stacks[move[1]-1] = stacks[move[1]-1][:moving_stack_len-move[0]]

        # Set "to stack" with moving_stack
        stacks[move[2]-1] = stacks[move[2]-1] + moving_stack
        print(stacks)

    for stack in stacks:
        print(stack[len(stack)-1], end='')
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('stacks')
    parser.add_argument('instructions')
    args = parser.parse_args()
    main(args.stacks, args.instructions)