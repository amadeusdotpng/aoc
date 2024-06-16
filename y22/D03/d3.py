priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main(file):
    with open(file, 'r') as r:
        lines = r.readlines()
        sum = 0

        for i in range(0, len(lines), 3):
            l1 = lines[i+0].strip()
            l2 = lines[i+1].strip()
            l3 = lines[i+2].strip()

            repeating_char = ''
            for c in l1:
                if (c in l2) and (c in l3):
                    repeating_char = c

            for i in range(len(priority)):
                if repeating_char == priority[i]:
                    sum += i+1
        
        print(sum)


if __name__ == '__main__':
    main('input.txt')