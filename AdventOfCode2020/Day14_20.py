# Advent of Code 2020 - Day 14

# Author:   Rachael Judy
# Date:     12/14/2020
# Purpose:  Part 1 - apply bitmasks to value where 0 and 1 overwrite and x leaves
#           Part 2 - apply bitmask to address where 0 leaves, 1 overwrites, and x switches to every possible

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# SET phase
phase = 1

# read instructions
lines = parseMod.readCSV_row('data/14masks.csv', '\n')

mem = {}
if phase == 1:
    # go through each line
    for instr in lines:
        content = instr.split(' ')
        # parse mask
        if content[0] == 'mask':
            mask_0 = 0x0000000000000000
            mask_1 = 0x0000000000000000
            # create mask for each stage
            for digit, bit in enumerate(content[2]):
                if bit == '1':  # set to ones
                    mask_0 = mask_0 | (1 << (35-digit))
                    mask_1 = mask_1 | (1 << (35-digit))
                elif bit == '0':  # set to zeros
                    mask_0 = mask_0 & (2**36 - 2**(35 - digit))
                    mask_1 = mask_1 & (2**36 - 2**(35 - digit))
                elif bit == 'X':  # set the and mask to one to stay and the or mask to zeros to not change
                    mask_0 = mask_0 = mask_0 | (1 << (35-digit))
                    mask_1 = mask_1 & (2 ** 36 - 2 ** (35 - digit))

        # assign value to memory
        else:  # memory assignment
            address = int(content[0][4:-1])
            value = (int(content[2]))
            value = ((mask_0) & value) | (mask_1)  # mask it
            mem[address] = value  # assign

# part 2
else:
    for instr in lines:
        content = instr.split(' ')
        # parse mask
        if content[0] == 'mask':
            masks_0 = []
            masks_1 = []
            mask_initial_0 = 0x00000000000000
            mask_initial_1 = 0x00000000000000

            # get the initial masks
            for digit, bit in enumerate(content[2]):
                if bit == '1':  # set ones
                    mask_initial_0 = mask_initial_0 | (1 << (35-digit))
                    mask_initial_1 = mask_initial_1 | (1 << (35-digit))
                elif bit == '0':  # if a zero, or then and
                    mask_initial_0 = mask_initial_0 & (2**36 - 2**(35 - digit))
                    mask_initial_1 = mask_initial_1 | (1 << (35-digit))
                else:  # bit == 'X' - first will set, second will vary
                    mask_initial_0 = mask_initial_0 | (1 << (35-digit))  # ones
                    mask_initial_1 = mask_initial_1 & (2 ** 36 - 2 ** (35 - digit))  # zeros
            masks_0.append(mask_initial_0)
            masks_1.append(mask_initial_1)

            # generate the bit masks that will be used
            for digit, bit in enumerate(content[2]):
                if bit == 'X':  # start new loop
                    temp_masks_0 = []
                    temp_masks_1 = []
                    for mask_0, mask_1 in zip(masks_0, masks_1):
                        mask_1 = mask_1 | (1 << (35-digit))  # add making each digit to and with a one
                        temp_masks_0.append(mask_0)
                        temp_masks_1.append(mask_1)
                    masks_0.extend(temp_masks_0)
                    masks_1.extend(temp_masks_1)

        # assign value to memory
        else:  # memory assignment for each mask
            value = (int(content[2]))
            # run through all possible masks
            for mask_0, mask_1 in zip(masks_0, masks_1):
                address = int(content[0][4:-1])
                address = (address | mask_0) & mask_1  # for each mask

                mem[address] = value

# display sum
print(sum(mem.values()))
