# Advent of Code 2018 - Day 2

# Author:   Rachael Judy
# Date:     12/15/2020
# Purpose:  Compute checksum (number of ids with exactly two or exactly three multiplied)
#           Find id off by one letter

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

boxes = parseMod.readCSV_row('data/2boxes.csv', '\n')

# part 1
twos_overall, threes_overall = 0, 0
for box in boxes:
    twos, threes = 0, 0
    for letter in range(ord('a'), ord('z')+1):
        if box.count(chr(letter)) == 2:
            twos += 1
        if box.count(chr(letter)) == 3:
            threes += 1
    twos_overall += (twos > 0)
    threes_overall += (threes > 0)

print("Part 1: ", twos_overall*threes_overall)

# part 2
for box1 in boxes:
    for box2 in boxes:  # look at each combo
        ans = []
        if box1 != box2:
            # count mismatch and mismatch character
            mismatch = 0
            mismatch_c = ''
            for char_1, char_2 in zip(box1, box2):
                if char_1 != char_2:
                    mismatch += 1
                    mismatch_c = char_1
            if mismatch == 1: # found it
                ans = [box1, box2]
                break

    if len(ans): break

# bit of a cheat, if not the first occurrence of the mismatch, won't replace the right one
# should display the ans instead and then remove the different character
print("Part 2: ", ans[0].replace(mismatch_c, '', 1))