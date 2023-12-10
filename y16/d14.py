from hashlib import md5
from functools import cache

@cache
def generate_hashA(inp: str):
    hash_ = md5(inp.encode()).hexdigest()
    return hash_

@cache
def generate_hashB(inp: str):
    hash_ = md5(inp.encode()).hexdigest()
    for _ in range(2016):
        hash_ = md5(hash_.encode()).hexdigest()
    return hash_

@cache
def check_five_char(inp: str, char: str):
    for i in range(len(inp)-5):
        characters = set([c for c in inp[i:i+5]])
        if len(characters) == 1 and char in characters:
            return True
    return False

def next_thousandA(input: str, start: int, char: str):
    for i in range(1, 1001):
        key = f'{input}{start+i}'
        hash_ = generate_hashA(key)
        if check_five_char(hash_, char):
            return (key, hash_)
    return False

def next_thousandB(input: str, start: int, char: str):
    for i in range(1, 1001):
        key = f'{input}{start+i}'
        hash_ = generate_hashB(key)
        if check_five_char(hash_, char):
            return (key, hash_)
    return False

def sol(input: str, gen, next_thousand):
    n = 0
    keys = set()
    while True:
        key = f'{input}{n}'
        hash_ = gen(key)
        for i in range(len(hash_)-3):
            if len(set([c for c in hash_[i:i+3]])) == 1 and (pair := next_thousand(input, n, hash_[i])):
                print(key, hash_[i], hash_, pair, end='\r')
                keys.add(key)
                break
        if len(keys) == 64:
            print('')
            return n
        n += 1

def partA(input: str):
    return sol(input, generate_hashA, next_thousandA)

def partB(input: str):
    return sol(input, generate_hashB, next_thousandB)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd14.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
