import argparse

def main(input):
    with open(input, 'r') as r:
        monkey_instructions = [i.split('\n') for i in r.read().split('\n\n')]
        monkey_items = []
        monkey_inspects = [0 for i in range(len(monkey_instructions))]
        # MONKEY LAYOUT:
        # MONKEY NUMBER, STARTING ITEMS, OPERATION, DIVISIBILITY, TRUE, FALSE
        
        for monkey in monkey_instructions:                                # ADD ITEMS TO EACH MONKEY
            monkey_items.append([int(i) for i in monkey[1].split(', ')])

        print('')
        for i in range(10000):
            print('\rRound: {}'.format(i+1), end='')
            for monkey in monkey_instructions:                                
                # OPERATE ON ITEMS FOR EACH MONKEY
                monkey_operate(monkey, monkey_items, monkey_inspects)
            # print(monkey_items)
        
        print('')
        monkey_inspects.sort()
        monkey_inspects = monkey_inspects[::-1]
        print(monkey_inspects)
        print(monkey_inspects[0]*monkey_inspects[1])

def monkey_operate(m, items, inspects):
    monkey_number = int(m[0])
    for item in items[monkey_number]:

        # OPERATE ON THE ITEMS 
        monkey_operation = m[2].split(' ') 
        if monkey_operation[1] == 'old':
            old_item = item
            item *= item
        elif monkey_operation[0] == '*':
            item *= int(monkey_operation[1])
        elif monkey_operation[0] == '+':
            item += int(monkey_operation[1])

        # # DIVIDE BECAUSE ITEM DIDN'T GET DAMAGED
        # item = item//3
        # item = item % 96577

        # TEST ITEMS
        if int(item) % int(m[3]) == 0:
            items[int(m[4])].append(item % 9699690)
        else:
            items[int(m[5])].append(item % 9699690)

        # ADD ONE TO INSPECT COUNT
        inspects[monkey_number] += 1
        
    items[monkey_number] = []

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)