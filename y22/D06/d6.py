import argparse

def main(input):
    with open(input, 'r') as r:
        n = 14
        line = r.readlines()[0]
        stream = line[:n-1]
        line = line[n-1:]

        for c in line:
            stream += c
            substream = stream[len(stream)-n:]
            if len(set(substream)) == n:
                print(substream)
                print(len(stream))
                break 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    
    args = parser.parse_args()
    main(args.input)