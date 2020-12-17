# Advent of Code 2020 - Day 17

# Author:   Rachael Judy
# Date:     12/17/2020
# Purpose:  Find number of active cubes in three and four dimensional space after six phases

import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


def check_adj_3d(x, y, z):
    global new_grid
    adj = 0
    adjacency_objects = [[i, j, k] for i in [x-1, x, x+1]
           for j in [y-1, y, y+1]
           for k in [z-1, z, z+1]]
    for p in adjacency_objects:
        adj += (new_grid[p[2]][p[1]][p[0]] == '#')

    return adj - (new_grid[z][y][x] == '#')


# checks on 4D adjacencies, virtually identical to 3
def check_adj_4d(x, y, z, w):
    global new_grid
    adj = 0
    adjacency_objects = [[i, j, k, l] for i in [x-1, x, x+1]
           for j in [y-1, y, y+1]
           for k in [z-1, z, z+1]
           for l in [w-1, w, w+1]]
    for p in adjacency_objects:
        adj += (new_grid[p[3]][p[2]][p[1]][p[0]] == '#')

    return adj - (new_grid[w][z][y][x] == '#')


layer_0 = parseMod.readCSV_row('data/17activity.csv')

# part 1
global grid, new_grid
# set up initial state
grid = [[['.' for i in range(22)] for j in range(22)] for k in range(15)]
for x in range(7, 7+len(layer_0[0])):
    for y in range(7, 7+len(layer_0)):
        grid[7][y][x] = layer_0[y-7][x-7]

# do iterations
for it in range(6):
    new_grid = copy.deepcopy(grid)
    for z in range(6-it, 9+it):
        for y in range(1, len(grid[0]) - 1):
            for x in range(1, len(grid[0][0]) - 1):
                adj = check_adj_3d(x, y, z)
                if new_grid[z][y][x] == '#' and not (adj == 2 or adj == 3):
                    grid[z][y][x] = '.'
                elif new_grid[z][y][x] == '.' and adj == 3:
                    grid[z][y][x] = '#'

count = sum([(grid[z][y][x] == '#') for x in range(len(grid[0][0]))
             for y in range(len(grid[0]))
             for z in range(len(grid))])
print("Part 1: ", count)


# part 2 - identical but with extra dimension
grid = [[[['.' for i in range(22)] for j in range(22)] for k in range(15)] for h in range(15)]
for x in range(7, 7+len(layer_0[0])):
    for y in range(7, 7+len(layer_0)):
        grid[7][7][y][x] = layer_0[y-7][x-7]

for it in range(6):
    new_grid = copy.deepcopy(grid)
    for w in range(6-it, 9+it):
        for z in range(6-it, 9+it):
            for y in range(1, len(grid[0][0]) - 1):
                for x in range(1, len(grid[0][0][0]) - 1):
                    adj = check_adj_4d(x, y, z, w)
                    if new_grid[w][z][y][x] == '#' and not (adj == 2 or adj == 3):
                        grid[w][z][y][x] = '.'
                    elif new_grid[w][z][y][x] == '.' and adj == 3:
                        grid[w][z][y][x] = '#'

count = sum([(grid[w][z][y][x] == '#') for x in range(len(grid[0][0][0]))
                                        for y in range(len(grid[0][0]))
                                        for z in range(len(grid[0]))
                                        for w in range(len(grid))])
print("Part 2: ", count)
