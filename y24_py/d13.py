import re

def row_multiplication(C, R):
    return [C*n for n in R]

def row_addition(R_0, R_1):
    return [n_0 + n_1 for n_0, n_1 in zip(R_0, R_1)]

def gauss_jordan(_M):
    M = _M[::]
    n_rows = len(M)
    for i in range(n_rows):
        M[i] = row_multiplication(1/M[i][i], M[i])
        for j in range(1,n_rows):
            inverse = row_multiplication(-M[(i+j)%n_rows][i], M[i])
            M[(i+j)%n_rows] = row_addition(M[(i+j)%n_rows], inverse)
    return M


def partA(inp: str):
    configurations = inp.split('\n\n')
    cost = 0
    for config in configurations:
        config = config.splitlines()
        A = list(int(n) for n in re.findall(r'\d+', config[0]))
        B = list(int(n) for n in re.findall(r'\d+', config[1]))
        P = list(int(n) for n in re.findall(r'\d+', config[2]))

        M = [[A[0], B[0], P[0]],[A[1], B[1], P[1]]]
        S = gauss_jordan(M)
        n, m = round(S[0][-1]), round(S[1][-1])

        if (n * A[0] + m * B[0] == P[0] and n * A[1] + m * B[1] == P[1] and n >= 0 and m >= 0):
            cost += 3 * n + m
    return cost

def partB(inp: str):
    configurations = inp.split('\n\n')
    cost = 0
    for config in configurations:
        config = config.splitlines()
        A = list(int(n) for n in re.findall(r'\d+', config[0]))
        B = list(int(n) for n in re.findall(r'\d+', config[1]))
        P = list(int(n)+10000000000000 for n in re.findall(r'\d+', config[2]))

        M = [[A[0], B[0], P[0]],[A[1], B[1], P[1]]]
        S = gauss_jordan(M)
        n, m = round(S[0][-1]), round(S[1][-1])

        if n < 0 or m < 0:
            print(S[0])
            print(S[1])
            print()

        if (n * A[0] + m * B[0] == P[0] and n * A[1] + m * B[1] == P[1] and n >= 0 and m >= 0):
            cost += 3 * n + m

    return cost

if __name__ == "__main__":
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd13.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
