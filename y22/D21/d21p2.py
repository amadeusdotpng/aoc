from collections import deque
input = [line.strip().split(': ') for line in open(0).readlines()]
D = {}
for monkey, expression in input:
    D[monkey] = expression
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def evaluate(a, b, operator):
    if operator == '+':
        return str(a + b)
    if operator == '-':
        return str(a - b)
    if operator == '*':
        return str(a * b)
    if operator == '/':
        return str(a / b)

def solve(start):
    Q = deque()
    Q.append(start)
    target_var = 'humn'
    humn_order = []
    while Q:
        monkey = Q.pop()
        expression = D[monkey]
        # print('Monkey: {:10} Expression: {}'.format(monkey,  expression))

        if is_number(expression):
            continue

        expression = expression.split(' ')
        Q.append(monkey)
        if expression[0] == target_var:
            humn_order.append((expression[1], expression[2]))
            Q.pop()
            Q.append(expression[2])
            target_var = monkey
            continue

        elif expression[2] == target_var:
            humn_order.append((expression[1], expression[0]))
            Q.pop()
            Q.append(expression[0])
            target_var = monkey
            continue
        
        if is_number(D[expression[0]]) and is_number(D[expression[2]]):
            D[monkey] = evaluate(float(D[expression[0]]), float(D[expression[2]]), expression[1]) 
            continue

        if not is_number(expression[0]):
            Q.append(expression[0])

        if not is_number(expression[2]):
            Q.append(expression[2])
    
    return humn_order

A, _, B= D['root'].split(' ')

L_A = solve(A)
L_B = solve(B)

L_full = []
equal_to = 0

if L_A:
    L_full = L_A
    equal_to = int(float(D[B]))
else:
    L_full = L_B
    equal_to = int(float(D[A]))

inverse = {'+': '-',
           '-': '+',
           '*': '/',
           '/': '*'}
print(equal_to)
for op, n in L_full[::-1]:
    equal_to = evaluate(float(equal_to), float(D[n]), inverse[op])
    # print('OP: {:5s} NUM: {:20s} VAR: {:10s} EQUAL: {}'.format(inverse[op], str(D[n]), n, str(equal_to)))

# print(L_full)
print()
# print(D['hdtb'])
print(equal_to)