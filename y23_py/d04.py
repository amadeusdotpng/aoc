def partA(input: str):
    input = input.splitlines()
    sum = 0
    for line in input:
        card_nums = line.split(': ')[-1]
        win_nums, my_nums = card_nums.split(' | ')
        win_nums = {int(n) for n in win_nums.split()}
        my_nums = {int(n) for n in my_nums.split()}

        score = 2**(len(win_nums & my_nums)-1)
        sum += score
    return sum

def partB(input: str):
    input = input.splitlines()
    cards = {}
    for id, line in enumerate(input):
        card_nums = line.split(': ')[-1]
        win_nums, my_nums = card_nums.split(' | ')
        win_nums = {int(n) for n in win_nums.split()}
        my_nums = {int(n) for n in my_nums.split()}

        cards[id] = (win_nums, my_nums, 1)
    
    for card in cards:
        win_nums, my_nums, n_owned = cards[card]
        score = len(win_nums & my_nums)
        for i in range(1, score+1):
            next_card = card+i
            next_win, next_nums, next_own = cards[next_card]
            cards[next_card] = (next_win, next_nums, next_own+n_owned)

    return sum(cards[card][-1] for card in cards)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd4.in'
    inp = open(infile).read().strip()
    print(f'A: {int(partA(inp[::]))}')
    print(f'B: {partB(inp[::])}')
    # Part A oneliner
    print(sum(2**(len(s[0]&s[1])-1) for s in [[set(c.split()) for c in l.split(': ')[-1].split(' | ')] for l in open(0)]))

