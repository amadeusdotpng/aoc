
def main():
    with open('calories.txt', 'r') as r:
        lines = r.readlines()
        sumCals = []
        sum = 0
        for line in lines:
            if line.strip() != '':
                sum += int(line.strip())
            else:
                sumCals.append(sum)
                sum = 0
        sumCals.append(sum)
        
        sumCals.sort(reverse=True)
        print(sumCals[0]+sumCals[1]+sumCals[2])
                


            


if __name__ == '__main__':
    main()
