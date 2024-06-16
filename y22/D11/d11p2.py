import numpy as np
import argparse

def main(input):
    with open(input, 'r') as r:
        monkey_instructions = [i.split('\n') for i in r.read().split('\n\n')]
        monkey_items = []
        monkey_inspects = [0 for i in range(len(monkey_instructions))]
        # MONKEY LAYOUT:
        # MONKEY NUMBER, STARTING ITEMS, OPERATION, DIVISIBILITY, TRUE, FALSE
        
        for monkey in monkey_instructions:                                # ADD ITEMS TO EACH MONKEY
            # print(monkey)
            monkey_items.append([int(i) for i in monkey[1].split(', ')])

        monkey_items = [np.array(items, dtype=int) for items in monkey_items]
        
        print('')
        for i in range(1):
            print('\rRound: {}'.format(i+1))
            for monkey in monkey_instructions:                                # OPERATE ON ITEMS FOR EACH MONKEY
                monkey_operate(monkey, monkey_items, monkey_inspects)
        
        print('\n',monkey_items)
        
        # print('')
        # monkey_inspects.sort()
        # monkey_inspects = monkey_inspects[::-1]
        # print(monkey_inspects)
        # print(monkey_inspects[0]*monkey_inspects[1])

def monkey_operate(m, items, inspects):
    monkey_number = int(m[0])

                 
    monkey_operation = m[2].split(' ')                                                  # OPERATE ON THE WORRY LEVELS
    print(monkey_number, monkey_operation, items[monkey_number])
    if monkey_operation[1] == 'old':
        items[monkey_number] = items[monkey_number] * items[monkey_number]
    elif monkey_operation[0] == '*':
        items[monkey_number] = items[monkey_number] * int(monkey_operation[1])
    elif monkey_operation[0] == '+':
        items[monkey_number] = items[monkey_number] + int(monkey_operation[1])
    print(items[monkey_number])
    print('')
    for item in items[monkey_number]:  
        if int(item) % int(m[3]) == 0:                                             # TEST
            items[int(m[4])] = np.append(items[int(m[4])], item)
        else:
            items[int(m[5])] = np.append(items[int(m[5])], item)
        inspects[monkey_number] += 1                   # ADD ONE TO INSPECT COUNT
        
    items[monkey_number] = np.array([], dtype=int)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)