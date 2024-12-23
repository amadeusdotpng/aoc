from collections import Counter, deque

def partA(inp: str):
    inp = inp.splitlines()

    S = 0
    for secret in inp:
        secret = int(secret)

        for _ in range(2000):
            secret = (secret ^ (secret << 6) ) % 2**24
            secret = (secret ^ (secret >> 5) ) % 2**24
            secret = (secret ^ (secret << 11)) % 2**24

        S += secret

    return S

def partB(inp: str):
    inp = inp.splitlines()

    shared_history_prices = Counter()
    for secret in inp:
        secret = int(secret)
        price = secret % 10

        history = deque()
        history_prices = Counter()

        for _ in range(3):
            next_secret = secret
            next_secret = (next_secret ^ next_secret << 6 ) % 2**24
            next_secret = (next_secret ^ next_secret >> 5 ) % 2**24
            next_secret = (next_secret ^ next_secret << 11) % 2**24

            change = (next_secret % 10) - (secret % 10)
            history.append(change)

            secret = next_secret

        for _ in range(2000-3):
            next_secret = secret
            next_secret = (next_secret ^ next_secret << 6 ) % 2**24
            next_secret = (next_secret ^ next_secret >> 5 ) % 2**24
            next_secret = (next_secret ^ next_secret << 11) % 2**24

            next_price = next_secret % 10
            change = next_price - price

            history.append(change)
            if len(history) > 4:
                history.popleft()

            tup_history = tuple(history)
            assert len(tup_history) == 4
            if tup_history not in history_prices:
                history_prices[tup_history] = next_price
        
            secret = next_secret
            price = next_price

        if shared_history_prices is None:
            shared_history_prices = history_prices
        else:
            shared_history_prices += history_prices

    return max(shared_history_prices.values())


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd22.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
