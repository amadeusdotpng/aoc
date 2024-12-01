import argparse

all_dirs = {}
sum_dirs = {}

def main(input):
    with open(input, 'r') as r:
        lines = r.readlines()
        
        current_dir = ''
        #   Gets each directory values and children
        for line in lines:
            line = line.strip().split(' ')

            if line[1] == 'cd' and line[2] != '..':  # Goes to a new directory
                if current_dir == '':
                    current_dir += line[2]
                else:
                    current_dir += '.'+line[2]
                all_dirs[current_dir] = 0

            elif line[1] == 'cd' and line[2] == '..':
                current_dir = '.'.join(current_dir.split('.')[:-1])

            elif line[0] != '$' and line[0] != 'dir':   # These are files
                all_dirs[current_dir] += int(line[0])
        

        # Calculates directory sizes when including subdirectories
        for dir in all_dirs:
            subs = get_sub_dirs(dir)
            sum_dirs[dir] = 0
            for sub in subs:
                sum_dirs[dir] += all_dirs[sub]


        # For Part 1
        total_sum = 0
        for dir in sum_dirs:
            sum = sum_dirs[dir]
            if sum <= 100000:
                total_sum += sum

        #-------------------------------#

        # For Part 2
        unused_space = 70000000 - int(sum_dirs['/'])
        deleted_space = 30000000 - unused_space

        dir_candidates = []
        for dir in sum_dirs:
            dir_size = sum_dirs[dir]
            if dir_size > deleted_space:
                dir_candidates.append(dir_size)

        print('Part 1: '+ str(total_sum))
        print('Part 2: '+ str(min(dir_candidates)))
        
def get_sub_dirs(d):
    l = []
    for subdir in all_dirs:
        if d in subdir:
            l.append(subdir)
    return l
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)