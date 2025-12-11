def parse(inp: str):
    D = {}
    for line in inp.split('\n'):
        k, v = line.split(': ')
        v = v.split()
        D[k] = v
    return D

def dp(S: str, G: str, D: dict[str, list[str]]) -> int:
    cache = {}
    def _dp(N: tuple[str, ...]) -> int:
        n = N[-1]
        if n in cache:
            return cache[n]

        if n == G:
            return 1
        
        if n not in D:
            return 0

        S = sum(_dp((*N, d)) for d in D[n] if d not in N)
        cache[n] = S

        return S

    return _dp((S,))

def partA(inp):
    return dp('you', 'out', inp)

def partB(inp):
    svr_to_fft = dp('svr', 'fft', inp)
    fft_to_dac = dp('fft', 'dac', inp)
    dac_to_out = dp('dac', 'out', inp)

    svr_to_dac = dp('svr', 'dac', inp)
    dac_to_fft = dp('dac', 'fft', inp)
    fft_to_out = dp('fft', 'out', inp)

    return svr_to_fft * fft_to_dac * dac_to_out + svr_to_dac * dac_to_fft * fft_to_out
    

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd11.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(parse(inp[::]))}')
    print(f'B: {partB(parse(inp[::]))}')
