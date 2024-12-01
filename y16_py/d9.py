def partA(input: str):
    count = 0
    i = 0
    while i < len(input):
        if input[i] == '(':
            lookahead = 0
            i += 1
            lookahead += 1
            next = qty = ''
            while '0' <= input[i] <= '9':
                next += input[i]
                i += 1
                lookahead += 1

            if input[i] != 'x':
                count += lookahead
                continue
                
            i += 1
            lookahead += 1

            while '0' <= input[i] <= '9':
                qty += input[i]
                i+= 1
                lookahead += 1

            if input[i] != ')':
                count += lookahead
                continue

            i += 1
            lookahead += 1

            next, qty = int(next), int(qty)
            count += next*qty
            i += next
        else:
            count += 1
            i+=1
    return count

def partB(input: str):
    return getLength(input)

def getLength(input: str):
    count = 0
    i = 0
    while i < len(input):
        if input[i] != '(':
            count += 1
            i += 1
            continue
        else:
            lookahead = 0
            next = qty = ''

            i += 1
            lookahead += 1
            while '0' <= input[i] <= '9':
                next += input[i]
                i += 1
                lookahead += 1

            if input[i] != 'x':
                count += lookahead
                continue

            i += 1
            lookahead += 1
            while '0' <= input[i] <= '9':
                qty += input[i]
                i += 1
                lookahead += 1

            if input[i] != ')':
                count += lookahead
                continue

            i += 1
            lookahead += 1
            next, qty = int(next), int(qty)
            substring_length = getLength(input[i:i+next])
            count += qty*substring_length
            i += next
    return count

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd9.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
