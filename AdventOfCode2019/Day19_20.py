# Advent of Code 2019 - Day 17

# Author:   Rachael Judy
# Date:     12/10/2020
# Purpose:  Find space affected by beam in 50x50 grid and find first coordinates (distance need)
#           to fit in 100x100 grid (upper left)

import os
import sys

import queue

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod
from intcodecomputer import Computer

# read drone instructions - each run takes one coordinate pair
instructions = parseMod.readCSVInts('data/19drone.csv')

# part 1 - find number of spaces affected in 50x50 range
beam_map = [[0 for i in range(50)] for j in range(50)]
count = 0
inputQ = queue.SimpleQueue()
for y in range(50):
    for x in range(50):
        drone = Computer(instructions)  # must recreate instance each time

        # put coordinates into input and get info
        inputQ.put(x)
        inputQ.put(y)
        beam_map[y][x] = drone.processInput(inputQ)[0]

        count += beam_map[y][x]  # if beam has affect, will increment

# display beam
for row in beam_map:
    for x in row:
        print(x, end='')
    print()
print("Part 1: ", count)
print()

# part 2 - find spot where 100 by 100 square can fit, reset map,
# find space via slope analysis and experimentation
beam_map = [[0 for i in range(120)] for j in range(120)]
inputQ = queue.SimpleQueue()
xlower, ylower = 1400, 680  # mess with these parameters to find the correct 120 x 120 segment
for y in range(ylower, ylower+len(beam_map)):
    for x in range(xlower, xlower+len(beam_map[0])):
        drone = Computer(instructions)

        inputQ.put(x)
        inputQ.put(y)

        beam_map[y-ylower][x-xlower] = drone.processInput(inputQ)[0]

# display section of interest
for row in beam_map:
    for x in row:
        print(x, end='')
    print()

# look through for correct grid
found = False
urx, llx = 0, 0
for y in range(len(beam_map)):  # go top to bottom
    for x in range(len(beam_map[0])-1, -1, -1):  # right to left
        if x >= 99 and beam_map[y][x] == 1:  # check if meets conditions to fit in 100x100
            if beam_map[y+99][x-99] == 1:
                ury = y
                llx = x-99
                found = True
                break
    if found:
        break

# offset by shifted amount of focused grid
ury += ylower
llx += xlower

# display
print("Upper left coordinates: ", llx, ury)
print("Part 2: ", llx*10000+ury)
