def partA(input: str):
    input = input.splitlines()
    sum = 0
    for room in input:
        parts = room.split('-')
        letters, id_checksum = parts[:-1], parts[-1]
        letters = ''.join(letters)
        id, checksum = id_checksum.split('[')
        checksum = checksum[:-1]
        letters_dict = {}
        for c in letters:
            letters_dict[c] = letters_dict.get(c, 0) + 1
        letters_sorted = sorted(letters_dict.items(), key=lambda x: (-x[1], x[0]))[:5]
        common = ''.join(s[0] for s in letters_sorted)
        sum += int(id) if common == checksum else 0
    return sum

def partB(input: str):
    input = input.splitlines()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for room in input:
        parts = room.split('-')
        letters, id_checksum = parts[:-1], parts[-1]
        letters = ''.join(letters)
        id, checksum = id_checksum.split('[')
        checksum = checksum[:-1]
        letters_dict = {}
        for c in letters:
            letters_dict[c] = letters_dict.get(c, 0) + 1
        letters_sorted = sorted(letters_dict.items(), key=lambda x: (-x[1], x[0]))[:5]
        common = ''.join(s[0] for s in letters_sorted)
        if common == checksum:
            new_name = ""
            for c in letters:
                new_name += alphabet[(alphabet.index(c) + int(id)) % len(alphabet)]
            if 'northpole' in new_name:
                return (new_name, id)
            


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd0.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
