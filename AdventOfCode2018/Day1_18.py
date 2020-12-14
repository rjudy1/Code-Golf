# Advent of Code 2018 - Day 1

# Author:   Rachael Judy
# Date:
# Purpose:


import os
import sys
import math

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

changes = parseMod.readCSV('data/1offset.csv')

# part 1
print("Part 1: ", sum(changes))

# part 2 - slow, maybe fix it later
x = 0
used = [x]
end, round = False, 0
while True:
    for i in changes:
        x += i
        if x in used:  # found repetition
            end = True
            break
        elif not round:  # will eventually start pattern over, so need only first set
            used.append(x)
    round += 1
    if end: break

print("Part 2: ", x)
