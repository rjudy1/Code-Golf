# Advent of Code 2018 - Day 3

# Author:   Rachael Judy
# Date:     12/15/2020
# Purpose:  Count squares of grid that are used multiple times and find the claim that is used only once

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# get input
recommendations = parseMod.readCSV_rowEl('data/3cuts.csv')

# populate fabric grid
fabric = [[0 for j in range(1200)] for i in range(1200)]
for suggestion in recommendations:
    position = suggestion[2].strip(':').split(',')  # third argument is position of top left
    dimensions = suggestion[3].split('x')  # fourth argument is dimension

    # increment the sea_monster_count on section being covered
    for y in range(int(position[1]), int(position[1]) + int(dimensions[1])):
        for x in range(int(position[0]), int(position[0]) + int(dimensions[0])):
            fabric[y][x] += 1

# sea_monster_count how many have more than one claims
count_overlaps = 0
for y in range(len(fabric)):
    for x in range(len(fabric[0])):
        if fabric[y][x] >= 2:
            count_overlaps += 1

print("Part 1: ", count_overlaps)

# part 2
# find recommendation that doesn't disagree with anyone else
for suggestion in recommendations:
    position = suggestion[2].strip(':').split(',')
    dimensions = suggestion[3].split('x')

    not_overlapped = True
    for y in range(int(position[1]), int(position[1]) + int(dimensions[1])):
        for x in range(int(position[0]), int(position[0]) + int(dimensions[0])):
            if fabric[y][x] > 1:  # already occupied
                not_overlapped = False

    if not_overlapped:
        print("Part 2: ", suggestion[0])
        break
