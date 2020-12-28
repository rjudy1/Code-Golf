# Advent of Code 2018 - Day 18

# Author:   Rachael Judy
# Date:     12/28/2020
# Purpose:  Simulate forestry pattern over 10 time steps, and then find its value at 1B time steps (p2 takes 20s)

import os, sys
from copy import deepcopy
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


def check_adj(x, y, array):  # count the number of each type adjacent
    types = ['.', '|', '#']
    counts = [0, 0, 0]  # open, trees, lumber
    for j in [y-1, y, y+1]:
        for i in [x-1, x, x+1]:
            if not (i==x and j==y) and 0<=j<len(array) and 0<=i<len(array[0]):
                for t in range(3):
                    counts[t] += 1 if array[j][i] == types[t] else 0

    return counts


def get_value(array):  # compute value of area by multiplying tree by lumberyard count
    trees, lumberyards = 0, 0
    for row in array:
        trees += row.count('|')
        lumberyards += row.count('#')

    return trees*lumberyards


woods = parseMod.readCSV_row('data/18map.csv', '\n')
for i, line in enumerate(woods):
    woods[i] = [c for c in line]

# simulate forest, tracking wood values
values = list()
for time in range(800):  # 800 should be enough to find the pattern
    copy_woods = deepcopy(woods)
    for y in range(len(woods)):
        for x in range(len(woods[0])):
            adj = check_adj(x, y, copy_woods)
            if copy_woods[y][x] == '.' and adj[1] >= 3:
                woods[y][x] = '|'
            elif copy_woods[y][x] == '|' and adj[2] >= 3:
                woods[y][x] = '#'
            elif copy_woods[y][x] == '#' and not (adj[1] >= 1 and adj[2] >= 1):
                woods[y][x] = '.'

    if time == 9:  # after 10 time steps, part 1 is complete
        print('part 1: ', get_value(woods))
    values.append(get_value(woods))  # store the values to look for pattern

# part 2 - find value of 1 bil steps
repeat_length, pattern_start = 0, 0
for shift in range(len(values)):  # check groups of 10 for repetition
    test = values[shift:shift+10]  # look for a match to it
    for x in range(shift+10, len(values)-10):
        if values[x:x+10] == test:  # if match found, note how far the shift was and where the pattern started
            repeat_length = x - shift
            pattern_start = shift
            # note what the 1B value would be (shift one because of 0 index)
            print('part 2: ', values[pattern_start + ((1000000000 - 1 - pattern_start) % repeat_length)])
            exit(0)
