def partA(input: str):
    input = input.splitlines()
    freq = [dict() for _ in range(len(input[0]))]
    for line in input:
        # print(line)
        for index, char in enumerate(line):
            # print(index, char)
            count = freq[index].get(char, 0)
            count += 1
            freq[index][char] = count
    freq = [sorted(f.items(), key=lambda x: x[1], reverse=True)[0][0] for f in freq]
    return ''.join(freq)

def partB(input: str):
    input = input.splitlines()
    freq = [dict() for _ in range(len(input[0]))]
    for line in input:
        # print(line)
        for index, char in enumerate(line):
            # print(index, char)
            count = freq[index].get(char, 0)
            count += 1
            freq[index][char] = count
    freq = [sorted(f.items(), key=lambda x: x[1], reverse=True)[-1][0] for f in freq]
    return ''.join(freq)
    

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd6.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
