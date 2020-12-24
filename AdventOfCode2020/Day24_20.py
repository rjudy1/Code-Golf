# Advent of Code 2020 - Day 24

# Author:   Rachael Judy
# Date:     12/24/2020
# Purpose:  Find the initial pattern from the set of instructions and then flip tiles based on adjacencies

import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

inp = parseMod.readCSV_row('data/24tiles.csv', '\n')

# dictionary of dim by dim - row under would be dim -1 then dim again
dim = 200
# gets next index of interest based on direction
do_next = {
    'nw': lambda x: x - dim,
    'ne': lambda x: x - dim + 1,
    'w' : lambda x: x - 1,
    'e' : lambda x: x + 1,
    'sw': lambda x: x+dim - 1,
    'se': lambda x: x+dim
}

# read each line of the input and follow the instructions from keypoint to tile
black_tiles = set()
for line in inp:
    ptr = 0
    keypoint = dim*dim/2  # a centerpoint that should allow for enough shifts in any direction
    while ptr != len(line):  # collect each instruction from the line, following to end
        if line[ptr] == 'n' or line[ptr] == 's':  # if ne, se, nw, sw
            instr = line[ptr] + line[ptr+1]
            ptr += 2
        else:  # w or e
            instr = line[ptr]
            ptr += 1

        keypoint = do_next[instr](keypoint)  # follow the instruction

    # flip at endpoint
    if keypoint in black_tiles:
        black_tiles.remove(keypoint)
    else:
        black_tiles.add(keypoint)

print("part 1:", len(black_tiles))
print()

# part 2
# black tiles with 0 or >2 adjacent black tiles are flipped
# white tiles with exactly 2 adjacent black tiles are flipped
for day in range(1, 101):  # 100 days
    new_tiles = copy.deepcopy(black_tiles)
    for i in range(dim**2):  # go over the overall pattern
        adj = sum((do_next[x](i) in black_tiles) for x in do_next.keys())  # count black tiles adjacent
        if i in black_tiles and (adj == 0 or adj > 2):  # black tile
            new_tiles.remove(i)
        elif i not in black_tiles and adj == 2:
            new_tiles.add(i)

    black_tiles = copy.deepcopy(new_tiles)  # overwrite the pattern
    if not day % 10:  # display every 10 days
        print(f"Day {day}: {len(new_tiles)}")

print("part 2: ", len(black_tiles))
