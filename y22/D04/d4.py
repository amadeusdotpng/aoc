import argparse

def main(file):
    with open(file, 'r') as r:
        lines = r.readlines()
        count = 0

        pairs = [i.strip().split(',') for i in lines]
        # print(pairs)

        for pair in pairs:
            pair = [i.split('-') for i in pair]
            # if   int(pair[0][0])-int(pair[1][0]) <= 0 and int(pair[0][1])-int(pair[1][1]) >= 0:
            #     count += 1
            # elif int(pair[0][0])-int(pair[1][0]) >= 0 and int(pair[0][1])-int(pair[1][1]) <= 0:
            #     count += 1

            if   int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][0]) <= int(pair[1][1]):
                count += 1
                print('overlapped')
            elif int(pair[0][1]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
                count += 1
                print("overlapped")
            elif int(pair[1][0]) >= int(pair[0][0]) and int(pair[1][0]) <= int(pair[0][1]):
                count += 1
                print('overlapped')
            elif int(pair[1][1]) >= int(pair[0][0]) and int(pair[1][1]) <= int(pair[0][1]):
                count+=1
                print("overlapped")
            print(pair)
        
        print(count)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    main(args.filename)