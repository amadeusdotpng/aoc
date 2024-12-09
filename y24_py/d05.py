from collections import defaultdict

def check_update(update, orders_dict):
    for i in range(len(update)-1):
        current = update[i]
        for j in range(i+1, len(update)):
            compare = update[j]

            if compare in orders_dict[current]:
                return None
    return update[int(len(update)/2)]

def partA(inp: str):
    orders, updates = inp.split('\n\n')
    orders = [tuple(map(int, line.split('|'))) for line in orders.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates.splitlines()]
    
    orders_dict = defaultdict(set)
    for left, right in orders:
        orders_dict[right].add(left)

    S = 0
    for update in updates:
        if (n := check_update(update, orders_dict)) is not None:
            S += n

    return S

def sort_update(update, orders_dict):
    sorted_update = [update[0]]
    for n in update[1:]:
        insert_index = None
        for i in range(len(sorted_update)):
            current = sorted_update[i]
            if n in orders_dict[current]:
                insert_index = i
                break
        if insert_index is None:
            sorted_update.append(n)
        else:
            sorted_update.insert(insert_index, n)
    return sorted_update

def partB(inp: str):
    orders, updates = inp.split('\n\n')
    orders = [tuple(map(int, line.split('|'))) for line in orders.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates.splitlines()]
    
    orders_dict = defaultdict(set)
    for left, right in orders:
        orders_dict[right].add(left)

    S = 0
    for update in updates:
        if (res := check_update(update, orders_dict)) is None:
            sorted_update = sort_update(update, orders_dict)
            S += sorted_update[int(len(sorted_update)/2)]

    return S


if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd05.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
