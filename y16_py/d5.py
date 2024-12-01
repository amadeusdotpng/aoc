from hashlib import md5

def partA(input: str):
    pass_ = ""
    index = 0
    while len(pass_) < 8:
        to_hash = input+str(index)
        hash = md5(to_hash.encode()).hexdigest()
        if hash[:5] == '00000':
            pass_ += hash[5]
        index += 1
    return pass_

def partB(input: str):
    pass_ = ["" for _ in range(8)]
    index = 0
    while len(''.join(pass_)) < 8:
        to_hash = input+str(index)
        hash = md5(to_hash.encode()).hexdigest()
        if hash[:5] == '00000':
            try:
                pos = int(hash[5])
                if 0 <= pos <= 7 and not pass_[pos]:
                    pass_[pos] = hash[6]
            except:
                pass
        index += 1
    return ''.join(pass_)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd5.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
