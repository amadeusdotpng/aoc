
# BLOCK COORDS ARE (ROW, COLUMN)
blocks = [[0+0j, 0+1j, 0+2j, 0+3j],
          [0+1j, 1+0j, 1+1j, 1+2j, 2+1j],
          [0+0j, 0+1j, 0+2j, 1+2j, 2+2j],
          [0+0j, 1+0j, 2+0j, 3+0j],
          [0+0j, 0+1j, 1+0j, 1+1j]]

locked = set()
input = open(0).readline()
n_blocks = len(input.strip())*5
instruction_index = 0
print(n_blocks)

def move_block(b, inst):
    
    can_right = inst == '>'
    can_left = inst == '<'
    for coord in b:
        if inst == '>' and max(b, key=lambda n: n.imag).imag >= 6 or coord+1j in locked:
            can_right = False

        if inst == '<' and min(b, key=lambda n: n.imag).imag <= 0 or coord-1j in locked:
            can_left = False

    # Iterating through each coord of block
    for i in range(len(b)):
        if can_right:
            b[i] += 1j
        elif can_left:
            b[i] -= 1j
         
    # Check if the bottom most part is going to hit a locked block
    can_fall = True
    for coord in b:
        if coord-1 in locked or min(b, key=lambda n: n.real).real == 0:
            can_fall = False
    
    if can_fall:
        for i in range(len(b)):
            b[i] -= 1
    
    return can_fall


# Tetris simulation
for j in range(n_blocks):
    print(j, end='\r', flush=True)

    # Get Block
    block = blocks[j%len(blocks)][:]
    M = max(locked, key=lambda n: n.real, default=-1).real+1
    # print(j, block, M)

    # Set Block Position
    for i in range(len(block)):
        block[i] += (M+3)+2j
    # print(j, block, 'set', end='')

    # Move Block
    falling = True
    while falling:
        instruction = input[instruction_index%len(input)]
        instruction_index += 1
        falling = move_block(block, instruction)
        # print(j, block, instruction, end='')
        # Adds it to set of coords after done falling
        if not falling:
            for coord in block:
                locked.add(coord)
    # print()
    # print()

locked = list(locked)
locked.sort(key=lambda n: n.real)
# print(locked)
M = max(locked, key=lambda n: n.real).real
print()
print(int(M+1))
# for row in range(int(M),-1,-1):
#     print(str(row)+' ', end='')
#     for col in range(7):
#         if complex(row, col) in locked:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print()
            
        
