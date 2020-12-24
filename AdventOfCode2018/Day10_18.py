# Advent of Code 2018 - Day 10

# Author:   Rachael Judy
# Date:     12/23/2020
# Purpose:  Find where the stars align to letters and the time they do. Takes some squinting

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

inp = parseMod.readCSV_row('data/10stars.csv', '\n')
position_dict = []
for i in inp:
    x = int(i[10:16])
    y = int(i[18:24])
    velx = int(i[36:38])
    vely = int(i[40:42])

    position_dict.append([x, y, velx, vely])

# look for spot where they're closest over every move, 75 seems to do the trick
for t in range(100000):
    min_x = min([x for x,y,_,_ in position_dict])
    max_x = max([x for x,y,_,_ in position_dict])
    min_y = min([y for x,y,_,_ in position_dict])
    max_y = max([y for x,y,_,_ in position_dict])

    W = 75
    if min_x+W >= max_x and min_y + W >= max_y:
        print("time : ", t)  # min_x, max_x, min_y, max_y)
        # display yhe grid of positions
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                if (x, y) in [(px, py) for px, py, _, _ in position_dict]:
                    print('#', end='')
                else:
                    print('`', end='')
            print()

    # move each point according to its velocity and position
    for p in position_dict:
        p[0] += p[2]
        p[1] += p[3]