import argparse
import numpy as np
import cv2
from d12 import BFS
def main(input):
    with open(input, 'r') as r:
        gridmap = [[c for c in line.strip()] for line in r.readlines()]
        
    start = ()
    end = ()
    for y in range(len(gridmap)):
        for x in range(len(gridmap[y])):
            if gridmap[y][x] == 'S':
                start = (y,x)
                gridmap[y][x] = 'a'
            elif gridmap[y][x] == 'E':
                end = (y,x)
                gridmap[y][x] = 'z'
    
    
    path = BFS(gridmap, start, end)

    img = np.array([[np.full(3, (ord(c)-ord('a'))/26*255) for c in line] for line in gridmap], dtype=np.uint8)
    for i in range(len(path)):
        y = path[i][0]
        x = path[i][1]
        img[y][x] = np.array([0,0,255])
        cv2.imwrite('./frames/'+str(i)+'.png', cv2.resize(img, (0,0), fx=5, fy=5, interpolation=cv2.INTER_AREA))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('map')

    args = parser.parse_args()
    main(args.map)