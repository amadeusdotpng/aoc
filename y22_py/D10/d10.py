import argparse

def main(input):
    with open(input, 'r') as r:
        instructions = [line.strip().split(' ') for line in r.readlines()]
        x = 1
        cycle = 1
        cycle_index = 0
        addx_finished = False
        
        # signal_strengths = []

        while True:
            
            # # FOR PART 1
            # if cycle % 40 == 20:
            #     signal_strengths.append(cycle*x)
            
            if  ((cycle-1)%40) >= x-1 and ((cycle-1)%40) <= x+1:
                # print(cycle%40, x, instructions[cycle_index])
                print('#', end='')
            else:
                # print(cycle%40, x, instructions[cycle_index])
                print('.', end='')
            
            if cycle % 40 == 0:
                print('')

            if cycle % 240 == 0:
                print('')

            if cycle_index >= len(instructions):
                break

            cycle += 1
            

            if cycle_index < len(instructions) and instructions[cycle_index][0] == 'addx' and addx_finished == False:    # Cycle 1
                addx_finished = True
                continue                                        # End of Cycle 1            

            if cycle_index < len(instructions) and instructions[cycle_index][0] == 'addx' and addx_finished == True:     # Cycle 2
                addx_finished = False                                   
                x += int(instructions[cycle_index][1])
                cycle_index += 1
                continue                                        # End of Cycle 2

            if cycle_index < len(instructions) and instructions[cycle_index][0] == 'noop':
                cycle_index += 1
                continue

        # print(signal_strengths)
        # print(sum(signal_strengths))
            
            
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)