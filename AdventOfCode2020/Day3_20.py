# Advent of Code Day 3

# Author:   Rachael Judy
# Date:     12/3/2020
# Purpose:  Count Trees on Descent Through L->R duplicate map
# Note to self: try to generalize these where possible to speed up stage 2


import parseMod


# find trees on route
def countTrees(map, xStep, yStep):
    x = 0
    y = 0
    count = 0
    while y < len(map):
        if map[y][x] == '#':  # trees marked with hashtag
            count += 1
        x = (x+xStep) % len(map[0])
        y += yStep

    return count


# read in map to array
vmap = parseMod.readCSV_row('data/3maps.csv')

# compute trees on given paths
x = countTrees(vmap, 1, 1)
y = countTrees(vmap, 3, 1)  # from stage one
z = countTrees(vmap, 5, 1)
w = countTrees(vmap, 7, 1)
v = countTrees(vmap, 1, 2)
print("Single:", y)
print("Combo:", v*w*x*y*z)
