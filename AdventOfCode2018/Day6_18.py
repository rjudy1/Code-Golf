# Advent of Code 2018 - Day 6

# Author:   Rachael Judy
# Date:     12/22/2020
# Purpose:  Find largest non infinite area closest to one point
#           and largest area less than 10000 manhattan distances from all points

import copy
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# set phase
phase = 1

lines = parseMod.readCSV_row('data/6coords.csv', '\n')
coordinates = []
for line in lines:
    line = line.split()
    coordinates.append((int(line[0].strip(',')), int(line[1])))  # offset by 200 to ensure we have a wide area

if phase == 1:
    # check each point in the grid for closest - don't include equidistant points
    grid = [[(600, 600) for j in range(375)] for i in range(375)]
    grid = np.array(grid)
    repeat_use = {}
    for y1 in range(len(grid)):
        for x1 in range(len(grid[0])):
            for x, y in coordinates:
                if abs(x1-x) + abs(y1-y) < abs(x1-grid[y1][x1][0]) + abs(y1-grid[y1][x1][1]):
                    grid[y1][x1] = (x, y)
                elif abs(x1-x) + abs(y1-y) == abs(x1-grid[y1][x1][0]) + abs(y1-grid[y1][x1][1]):
                    repeat_use[(x1, y1)] = x, y

    # populate count and remove repeat uses
    coordinate_dict = {i: 0 for i in coordinates}
    for y1 in range(len(grid)):
        for x1 in range(len(grid[0])):
            if (x1, y1) not in repeat_use or (x1, y1) in repeat_use and (grid[y1][x1][0], (grid[y1][x1])[1]) not in repeat_use[(x1, y1)]:
                    coordinate_dict[(grid[y1][x1][0], (grid[y1][x1])[1])] += 1

    # eliminate edges as an option
    copy_coords = copy.deepcopy(coordinates)
    for x in range(len(grid[0])):
        if (grid[0][x][0], grid[0][x][1]) in copy_coords:
            copy_coords.remove((grid[0][x][0], grid[0][x][1]))
        if (grid[374][x][0], grid[374][x][1]) in copy_coords:
            copy_coords.remove((grid[374][x][0], grid[374][x][1]))
    for y in range(len(grid[0])):
        if (grid[y][0][0], grid[y][0][1]) in copy_coords:
            copy_coords.remove((grid[y][0][0], grid[y][0][1]))
        if (grid[y][374][0], grid[y][374][1]) in copy_coords:
            copy_coords.remove((grid[y][374][0], grid[y][374][1]))

    best_area = max(coordinate_dict[c] for c in copy_coords)
    print("part 1: ", best_area)

# part 2
else:
    # look at a bunch of coordinates and count if they are in range
    count = 0
    for y1 in range(-50, 450):
        for x1 in range(-50, 400):
            distance = sum(abs(y1-y) + abs(x1-x) for x,y in coordinates)
            count += distance < 10000
    print("part 2: ", count)
