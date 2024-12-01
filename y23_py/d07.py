def partA(input: str):
    input = input.splitlines()
    input = [(line.split()[0], int(line.split()[1])) for line in input]
    strength = {'A':12, 'K':11, 'Q':10, 'J':9, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0}
    scores = {}
    for hand in input:
        score = {}
        for card in hand[0]:
            s = score.get(card, 0)
            score[card] = s+1
        m = max(score.values())
        if m == 1:
            scores[hand[0]] = 0
        elif m == 2:
            L = len(set(list(hand[0])))
            if L == 4:
                scores[hand[0]] = 1
            elif L == 3:
                scores[hand[0]] = 2
        elif m == 3:
            L = len(set(list(hand[0])))
            if L == 3:
                scores[hand[0]] = 3
            elif L == 2:
                scores[hand[0]] = 4
        elif m == 4:
            scores[hand[0]] = 5
        elif m == 5:
            scores[hand[0]] = 6

    for i in range(len(input)):
        for j in range(len(input)-1):
            if i == j:
                continue
            
            score0 = scores[input[j][0]]
            score1 = scores[input[j+1][0]]

            if score0 > score1:
                input[j], input[j+1] = input[j+1], input[j]
                continue
            elif score0 < score1:
                continue
            else: 
                for k in range(len(input[j][0])):
                    if strength[input[j][0][k]] > strength[input[j+1][0][k]]:
                        input[j], input[j+1] = input[j+1], input[j]
                        break
                    elif strength[input[j][0][k]] < strength[input[j+1][0][k]]:
                        break
    score = 0
    for i, hand, in enumerate(input):
        score += hand[1]*(i+1)
    return score


def partB(input: str):
    input = input.splitlines()
    input = [(line.split()[0], int(line.split()[1])) for line in input]
    strength = {'A':12, 'K':11, 'Q':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1, 'J': 0}
    scores = {}
    for hand in input:
        score = {}
        for card in hand[0]:
            s = score.get(card, 0)
            score[card] = s+1

        m = 0
        c = 'J'
        for card in score:
            if card == 'J':
                continue
            if score[card] > m:
                m = score[card]
                c = card

        m += score.get('J', 0)
        if m == 1:
            scores[hand[0]] = 0
        elif m == 2:
            L = len(set(list(hand[0].replace('J', c))))
            if L == 4:
                scores[hand[0]] = 1
            elif L == 3:
                scores[hand[0]] = 2
        elif m == 3:
            L = len(set(list(hand[0].replace('J', c))))
            if L == 3:
                scores[hand[0]] = 3
            elif L == 2:
                scores[hand[0]] = 4
        elif m == 4:
            scores[hand[0]] = 5
        elif m == 5:
            scores[hand[0]] = 6

    for i in range(len(input)):
        for j in range(len(input)-1):
            if i == j:
                continue
            
            score0 = scores[input[j][0]]
            score1 = scores[input[j+1][0]]

            if score0 > score1:
                input[j], input[j+1] = input[j+1], input[j]
                continue
            elif score0 < score1:
                continue
            else: 
                for k in range(len(input[j][0])):
                    if strength[input[j][0][k]] > strength[input[j+1][0][k]]:
                        input[j], input[j+1] = input[j+1], input[j]
                        break
                    elif strength[input[j][0][k]] < strength[input[j+1][0][k]]:
                        break
    score = 0
    for i, hand, in enumerate(input):
        score += hand[1]*(i+1)
    return score

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd07.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
