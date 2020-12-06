# Advent of Code Day 3

# Author:   Rachael Judy
# Date:     12/3/2020
# Purpose:  Count Trees on Descent Through L->R duplicate map
# Note to self: try to generalize these where possible to speed up stage 2


import parseMod


# calculate next index at overflow
def nextIndex(currX, step, patternWid):
    if currX < patternWid - step:
        return currX + step
    else:
        return currX + step - patternWid


# find trees on route
def countTrees(map, xStep, yStep):
    x = 0
    y = 0
    count = 0
    while y < len(map):
        if map[y][x] == '#':  # trees marked with hashtag
            count += 1
        x = nextIndex(x, xStep, len(map[0]))
        y += yStep

    return count


# read in map to array
map = parseMod.readCSV_row('data/3maps.csv')

# compute trees on given paths
x = countTrees(map, 1, 1)
y = countTrees(map, 3, 1)  # from stage one
z = countTrees(map, 5, 1)
w = countTrees(map, 7, 1)
v = countTrees(map, 1, 2)
print("Single", y)
print("Combo", v*w*x*y*z)
