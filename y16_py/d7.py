def partA(input: str):
    input = input.splitlines()
    count = 0
    for line in input:
        ip = line.replace('[', ' ').replace(']', ' ').split()
        abba_in = False
        abba_out = False

        # check within brackets
        for i in range(1, len(ip), 2):
            for j in range(len(ip[i])-3):
                abba = ip[i][j:j+4]
                if abba[0] != abba[1] and abba[:2] == abba[::-1][:2]:
                    abba_in = True
                    break
            if abba_in:
                break
        if abba_in:
            continue

        for i in range(0, len(ip), 2):
            for j in range(len(ip[i])-3):
                abba = ip[i][j:j+4]
                if abba[0] != abba[1] and abba[:2] == abba[::-1][:2]:
                    abba_out = True
                    break
            if abba_out:
                break
        if abba_out:
            count += 1
    return count



def partB(input: str):
    input = input.splitlines()
    count = 0
    
    for line in input:
        ip = line.replace('[', ' ').replace(']', ' ').split()
        ABA = set()
        support = False

        # Check ABA outside brackets
        for i in range(0, len(ip), 2):
            for j in range(len(ip[i])-2):
                sub_string = ip[i][j:j+3]
                if sub_string[0] != sub_string[1] and sub_string[0] == sub_string[2]:
                    ABA.add((sub_string[0], sub_string[1]))

        # Check ABA inside brackets
        for i in range(1, len(ip), 2):
            for j in range(len(ip[i])-2):
                sub_string = ip[i][j:j+3]
                if (sub_string[1], sub_string[0]) in ABA and sub_string[0] == sub_string[2]:
                    support = True
                    break
            if support:
                break
        if support:
            count += 1
    return count

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd7.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
