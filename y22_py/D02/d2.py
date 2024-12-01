

def main(file):
    with open(file, 'r') as r:
        lines = r.readlines()
        score = 0
        print(lines)
        for l in lines:
            l = l.strip().split(' ')
            if      l[0] == 'A':        # ROCK
                if      l[1] == 'X':    # LOSE
                    score += 0+3
                elif    l[1] == 'Y':    # DRAW
                    score += 3+1
                elif    l[1] == 'Z':    # WIN
                    score += 6+2

            elif    l[0] == 'B':        # PAPER
                if      l[1] == 'X':    # LOSE
                    score += 0+1
                elif    l[1] == 'Y':    # DRAW
                    score += 3+2
                elif    l[1] == 'Z':    # WIN
                    score += 6+3
                    
            elif    l[0] == 'C':        # SCISSOR
                if      l[1] == 'X':    # LOSE
                    score += 0+2
                elif    l[1] == 'Y':    # DRAW
                    score += 3+3
                elif    l[1] == 'Z':    # WIN
                    score += 6+1

        print(score)

if __name__ == '__main__':
    main("input.txt")