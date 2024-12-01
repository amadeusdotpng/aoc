import argparse
import queue
def main(input):
    with open(input, 'r') as r:
        # Parse Input
        packets = [eval(line.strip()) for line in r.readlines() if len(line.strip()) > 0]
        packet_queue = queue.Queue()

        ################################## PART ONE ########################################

        sum = 0
        for i in range(0, len(packets), 2):
            lt = packets[i]
            rt = packets[i+1]
            index = i//2+1
            if compare(lt, rt):
                sum += index
        print(sum)

        ################################## PART TWO #######################################

        for packet in packets:
            packet_queue.put(packet)

        divider_one = [[2]]                                     # Marker ; part of part 2 challenge
        divider_two = [[6]]                                     # Marker ; part of part 2 challenge
        index_one = 0
        index_two = 0

        packet_queue.put(divider_one)     
        packet_queue.put(divider_two)

        ordered_packets = []
        ordered_packets.append(packet_queue.get())
        
        while not packet_queue.empty():
            current_packet = packet_queue.get()                 # Thing to Sort
            for i in range(len(ordered_packets)+1):
                if i == len(ordered_packets):
                    ordered_packets.insert(i, current_packet)
                    break

                right_packet = ordered_packets[i]               # current packet to compare with
                if compare(current_packet, right_packet):
                    ordered_packets.insert(i, current_packet)
                    break
        
        for i in range(len(ordered_packets)):                   # Get Divider Indexes
            if ordered_packets[i] == divider_one:
                index_one = i+1
            elif ordered_packets[i] == divider_two:
                index_two = i+1

        print(index_one*index_two)

################################### IMPORTANT FUNCTIONS ###############################################

def compare(lt, rt):
    result = 'continue'
    left = lt[::]
    right = rt[::]
    for i in range(min(len(left), len(right))):

        # Checks if it's mixed types
        if type(left[i]) == int and type(right[i]) == list:
            left[i] = [left[i]]
        elif type(left[i]) == list and type(right[i]) == int:
            right[i] = [right[i]]

        # If left and right are lists, do compare on the lists again, because the list might have a list inside it.
        if type(left[i]) == list and type(right[i]) == list:
            result = compare(left[i], right[i])

        if type(left[i]) == int and type(right[i]) == int:
            result = compare_int(left[i], right[i])

        # Result might not be true or false
        if result != 'continue':
            return result
    if len(left) < len(right):
        return True
    if len(left) > len(right):
        return False
    return 'continue'

def compare_int(left, right):
    if left < right:
        return True
    if left > right:
        return False
    return 'continue'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)