import argparse

def main(input):
    with open(input, 'r') as r:
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')

    args = parser.parse_args()
    main(args.input)

# Testing commit
