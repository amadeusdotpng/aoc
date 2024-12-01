
def partA(input: str):
    floors = [
        ['POG', 'PRG', 'THG', 'THM', 'RUG', 'RUM', 'COG', 'COM'],
        ['POM', 'PRM'],
        [],
        []]

def partB(input: str):
    pass

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd11.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
