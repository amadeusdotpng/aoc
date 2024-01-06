class Node:
    key: str
    value: int
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'({self.key}: {self.value})'

class LinkedList:
    root: Node
    def __init__(self):
        self.root = None

    def add(self, key: str, value: int):
        if not self.root:
            self.root = Node(key, value)
            return True

        current = self.root
        if current.key == key:
            current.value = value
            return True

        while (next := current.next):
            if next.key == key:
                next.value = value
                return True
            current = next

        current.next = Node(key, value)
        return True

    def remove(self, key: str):
        if self.root == None:
            return None

        current = self.root
        if current.key == key:
            self.root = current.next
            return current.value

        while (next := current.next):
            if next.key == key:
                current.next = next.next
                return next.value
            current = next

        return None

    def pop(self):
        if self.root == None:
            return None
        current = self.root
        self.root = current.next
        return current.value
        

def hash(S: str) -> int:
    V = 0
    for c in S:
        V = ((V+ord(c))*17)%256
    return V

def partA(input: str) -> int:
    S = input.split(',')
    return sum(hash(s) for s in S)

def partB(input: str) -> int:
    instructions = input.split(',')
    table = {}
    for i, instruction in enumerate(instructions):
        print(f'{instruction}: {i} out of {len(instructions)}', end='\r')
        if '=' in instruction:
            K, V = instruction.split('=')
            H = hash(K)

            if H not in table:
                table[H] = LinkedList()

            table[H].add(K,int(V))
        else:
            K = instruction.replace('-', '')
            H = hash(K)
            if H not in table:
                continue
            table[H].remove(K)

    sum = 0
    for H in table:
        i = 1
        while (V:=table[H].pop()):
            print((H+1), i, V)
            sum += (H+1)*V*i
            i += 1
    return sum

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd15.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
    print(hash("cm"))
