def partA(input: str):
    input = input.splitlines()
    ans = 0
    for line in input:
        vals = [int(n) for n in line.split()]
        last_vals = [vals[-1]]
        t = []
        while True:
            for i in range(len(vals)-1):
                t.append(vals[i+1]-vals[i])
            vals = t
            t = []
            last_vals.append(vals[-1])
            if all(n==0 for n in vals):
                break
        ans += sum(last_vals)
    return ans


def partB(input: str):
    input = input.splitlines()
    ans = 0
    for line in input:
        vals = [int(n) for n in line.split()]
        first_vals = [vals[0]]
        t = []
        while True:
            for i in range(len(vals)-1):
                t.append(vals[i+1]-vals[i])
            vals = t
            t = []
            first_vals.append(vals[0])
            if all(n==0 for n in vals):
                break
        first_vals = first_vals[::-1]
        curr_val = 0
        for v in first_vals:
            curr_val = v - curr_val
        ans += curr_val
    return ans

def refactored_partB(input: str):
    input = input.splitlines()
    ans = 0
    for line in input:
        vals = [int(n) for n in line.split()][::-1]
        last_vals = [vals[-1]]
        t = []
        while True:
            for i in range(len(vals)-1):
                t.append(vals[i+1]-vals[i])
            vals = t
            t = []
            last_vals.append(vals[-1])
            if all(n==0 for n in vals):
                break
        ans += sum(last_vals)
    return ans

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd09.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
    print(f'B: {refactored_partB(inp[::])}')
