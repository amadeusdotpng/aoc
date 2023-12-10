def partA(input: str):
    input = input.split('\n\n')
    seeds, categories = input[0], input[1:]
    seeds = [int(x) for x in seeds.split()]
    lookup = [[[int(x) for x in line.split()] for line in category.splitlines()] for category in categories]
    locations = set()
    for seed in seeds:
        current_location = seed
        for category in lookup:
            for ranges in category:
                if ranges[1] <= current_location <= ranges[1]+ranges[2]-1:
                    diff = ranges[0]-ranges[1]
                    current_location += diff
                    break
        locations.add(current_location)
    return min(locations)


def partB(input: str):
    input = input.split('\n\n')
    seeds, categories = input[0], input[1:]
    seeds = [int(x) for x in seeds.split()]
    lookup = [[[int(x) for x in line.split()] for line in category.splitlines()] for category in categories]
    locations = set()
    for i in range(0, len(seeds), 2):
        rs = {(seeds[i], seeds[i]+seeds[i+1]-1)}
        for category in lookup:
            fractures = []
            for loc_ranges in category:
                start = loc_ranges[1]
                end = loc_ranges[1]+loc_ranges[2]-1
                for r in rs:
                    if r[0] <= start <= r[1]:
                        fractures.append(start)
                    if r[0] <= end <= r[1]:
                        fractures.append(end)
                    
            new_rs = set()
            fractures.append(r[1])
            fractures = sorted(fractures)
            start = r[0]
            for f in fractures:
                new_rs.add((start, f))
                start = f

            rs = new_rs
            new_rs = set()
            for loc_ranges in category:
                for r in rs:
                    start = loc_ranges[1]
                    end = loc_ranges[1]+loc_ranges[2]-1
                    if start <= r[0] and r[1] <= end:
                        diff = loc_ranges[0]-loc_ranges[1]
                        new_rs.add((r[0]+diff, r[1]+diff))
                        break
            rs = new_rs
        for r in rs:
            locations.add(r[0])
    return min(locations)
                    
            
if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd5.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
