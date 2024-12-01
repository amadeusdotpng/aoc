def partA(input: str):
    input = input.splitlines()
    sum = 0
    for line in input:
        n = ''
        for c in line:
            if c.isdigit():
                n += c
                break
        for c in line[::-1]:
            if c.isdigit():
                n += c
                break
        sum += int(n)
    return sum

def partB(input: str):
    input = input.splitlines()
    sum = 0
    digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for line in input:
        n = a = b = ''
        a_break = b_break = False
        for c in line:
            a += c
            if c.isdigit():
                n += c
                break
            for key in digits:
                if key in a:
                    n += digits[key]
                    a_break = True
                    break
            if a_break:
                break
        for c in line[::-1]:
            b += c
            if c.isdigit():
                n += c
                break
            for key in digits:
                if key in b[::-1]:
                    n += digits[key]
                    b_break = True
                    break
            if b_break:
                break
        sum += int(n)
    return sum

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd1.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
