from collections import deque

def moveA(p, m, boxes, barriers):
    pr, pc = p
    mr, mc = m

    lookr, lookc = pr+mr, pc+mc
    boxes_moved = set()

    if (lookr, lookc) in barriers:
        return p, boxes

    while (lookr, lookc) in boxes:
        boxes_moved.add((lookr, lookc))

        lookr, lookc = lookr+mr, lookc+mc
        if (lookr, lookc) in barriers:
            return p, boxes

    new_boxes = {(boxr+mr, boxc+mc) for boxr, boxc in boxes_moved}
    boxes -= boxes_moved
    boxes |= new_boxes

    return (pr + mr, pc + mc), boxes

def partA(inp: str):
    grid, instructions = inp.split('\n\n')
    grid = [line for line in grid.splitlines()]
    instructions = ''.join(line for line in instructions.splitlines())

    boxes = set()
    barriers = set()
    pr, pc = None, None
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char == '@':
                pr, pc = r, c
                continue
            if char == 'O':
                boxes.add((r, c))
                continue
            if char == '#':
                barriers.add((r, c))
                continue

    for instruction in instructions:
        if instruction == '>':
            (pr, pc), boxes = moveA((pr, pc), (0, 1), boxes, barriers)
            continue
        if instruction == 'v':
            (pr, pc), boxes = moveA((pr, pc), (1, 0), boxes, barriers)
            continue
        if instruction == '<':
            (pr, pc), boxes = moveA((pr, pc), (0, -1), boxes, barriers)
            continue
        if instruction == '^':
            (pr, pc), boxes = moveA((pr, pc), (-1, 0), boxes, barriers)
            continue

    return sum(100 * pr + pc for pr, pc in boxes)

def move_horizontal(p, m, boxes, barriers):
    pr, pc = p

    lookr, lookc = pr, pc+m
    moved_boxes = set()

    if (lookr, lookc) in barriers:
        return p, boxes

    while (lookr, lookc) in boxes or (lookr, lookc-1) in boxes:
        if (lookr, lookc) in boxes:
            moved_boxes.add((lookr, lookc))
        if (lookr, lookc-1) in boxes:
            moved_boxes.add((lookr, lookc-1))

        lookr, lookc = lookr, lookc+2*m
        if (lookr, lookc) in barriers:
            return p, boxes

    new_boxes = {(boxr, boxc+m) for boxr, boxc in moved_boxes}

    for br, bc in moved_boxes:
        del boxes[(br, bc)]

    for br, bc in new_boxes:
        boxes[(br, bc)] = (br, bc+1)

    return (pr, pc + m), boxes

def move_vertical(p, m, boxes, barriers):
    pr, pc = p
    lookr, lookc = pr+m, pc

    if (lookr, lookc) in barriers:
        return p, boxes


    root_box = (
        (lookr, lookc) if (lookr, lookc) in boxes else
        (lookr, lookc-1) if (lookr, lookc-1) in boxes
        else None
    )

    if root_box is None:
        return (pr+m, pc), boxes

    er, ec = root_box
    if (
        (er+m, ec)   in barriers or
        (er+m, ec+1) in barriers
    ):
        return p, boxes

    Q = deque([root_box])
    X = set([root_box])

    while Q:
        br, bc = Q.popleft()
        edges = set()
        if (br+m, bc-1) in boxes: edges.add((br+m, bc-1))
        if (br+m, bc)   in boxes: edges.add((br+m, bc))
        if (br+m, bc+1) in boxes: edges.add((br+m, bc+1))

        for er, ec in edges:
            if (
                (er+m, ec)   in barriers or
                (er+m, ec+1) in barriers

            ):
                return p, boxes

            Q.append((er, ec))
            X.add((er, ec))

    new_boxes = {(boxr+m, boxc) for boxr, boxc in X}

    for br, bc in X:
        del boxes[(br, bc)]

    for br, bc in new_boxes:
        boxes[(br, bc)] = (br, bc+1)

    return (pr+m, pc), boxes

def partB(inp: str):
    grid, instructions = inp.split('\n\n')
    grid = [line for line in grid.splitlines()]
    instructions = ''.join(line for line in instructions.splitlines())

    boxes = {}
    barriers = set()
    pr, pc = None, None

    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char == '@':
                pr, pc = r, 2*c
                continue
            if char == 'O':
                boxes[(r, 2*c)] = (r, 2*c+1)
                continue
            if char == '#':
                barriers.add((r, 2*c))
                barriers.add((r, 2*c+1))
                continue

    for i, instruction in enumerate(instructions):
        if instruction == '>':
            (pr, pc), boxes = move_horizontal((pr, pc), 1, boxes, barriers)
        elif instruction == 'v':
            (pr, pc), boxes = move_vertical((pr, pc), 1, boxes, barriers)
        elif instruction == '<':
            (pr, pc), boxes = move_horizontal((pr, pc), -1, boxes, barriers)
        elif instruction == '^':
            (pr, pc), boxes = move_vertical((pr, pc), -1, boxes, barriers)

    return sum(100 * pr + pc for pr, pc in boxes)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd15.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
