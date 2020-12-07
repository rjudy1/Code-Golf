# Advent of Code 2020 - Day 5

# Author:   Rachael Judy
# Date:     12/5/2020
# Purpose:  Find the highest boarding pass ID (binary) and the missing one

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# get passes
plane = parseMod.readCSV_row('data/5boarding.csv')

# find lowest and highest id
ids = []
lowest = 1000
highest = 0
for seat in plane:
    # get row
    row = 0
    exp = len(seat[0:-3])
    for letter in seat[:-3]:
        exp -= 1
        row += ((letter == 'B') * 2**exp)

    # get column
    col = 0
    exp = len(seat[-3:])
    for letter in seat[-3:]:
        exp -= 1
        col += ((letter == 'R') * 2**exp)

    pass_id = row*8 + col

    """ 
    # for shorter id calculation without separation of row or column
    exp = len(seat)
    for letter in seat:
        exp -= 1
        pass_id += ((letter == 'R' or letter == 'B') * 2**exp)
    """

    # find min and max ids for part 2
    lowest = min(lowest, pass_id)
    highest = max(highest, pass_id)
    ids.append(row*8+col)

# find missing one
mine = 0
for bp in range(lowest, highest):
    if bp not in ids:
        mine = bp

# display
print("Highest ID: ", highest)
print("Missing ID: ", mine)
