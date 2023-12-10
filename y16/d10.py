def initialize(instruction_list):
    bots = {} # keeps track of what the bots are holding
    rules = {} # keeps track of which chip goes to which bot
    instruction_list = instruction_list.splitlines()
    for instruction in instruction_list:
        instruction = instruction.split()
        if instruction[0] == 'value':
            bot = int(instruction[5])
            chip = int(instruction[1])

            hands = bots.get(bot, [])
            hands.append(chip)
            bots[bot] = hands

        elif instruction[0] == 'bot':
            bot = int(instruction[1])
            low_to, high_to = int(instruction[6]), int(instruction[11])

            if instruction[5] == 'output' and instruction[10] == 'output':
                rules[bot] = [-(low_to+1), -(high_to+1)]
            if instruction[5] == 'output' and instruction[10] != 'output':
                rules[bot] = [-(low_to+1), high_to]
            if instruction[5] != 'output' and instruction[10] == 'output':
                rules[bot] = [low_to, -(high_to+1)]
            if instruction[5] != 'output' and instruction[10] != 'output':
                rules[bot] = [low_to, high_to]
    return bots, rules
    
def update(bots, rules, bot):
    low, high = sorted(bots[bot])
    bots[bot] = []
    low_bot, high_bot = rules[bot]
    low_hand, high_hand = bots.get(low_bot, []), bots.get(high_bot, [])
    low_hand.append(low); high_hand.append(high)
    bots[low_bot], bots[high_bot] = low_hand, high_hand

    # Part A
    # if low == 17 and high == 61:
        # print(bot)

    if len(bots[low_bot]) == 2 and low_bot >= 0:
        update(bots, rules, low_bot)
    if len(bots[high_bot]) == 2 and high_bot >= 0:
        update(bots, rules, high_bot)

def partA(input: str):
    bots, rules = initialize(input)
    starting_bot = 0
    for bot in bots:
        if len(bots[bot]) == 2:
            starting_bot = bot
            break

    update(bots, rules, starting_bot)
    return 161

def partB(input: str):
    bots, rules = initialize(input)
    starting_bot = 0
    for bot in bots:
        if len(bots[bot]) == 2:
            starting_bot = bot
            break

    update(bots, rules, starting_bot)
    return bots[-1][0]*bots[-2][0]*bots[-3][0]

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd10.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
