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

Q = deque()
Q.append('root')

while Q:
    monkey = Q.pop()
    expression = D[monkey]
    # print('Q: {:50s} Monkey: {:10} Expression: {}'.format(str(list(Q)), monkey,  expression))

    if is_number(expression):
        continue

    expression = expression.split(' ')
    
    if is_number(D[expression[0]]) and is_number(D[expression[2]]):
        D[monkey] = evaluate(float(D[expression[0]]), float(D[expression[2]]), expression[1]) 
        continue

    Q.append(monkey)

    if not expression[0].isnumeric():
        Q.append(expression[0])

    if not expression[2].isnumeric():
        Q.append(expression[2])

print(D['jhpn'])
print(D['jmsg'])
