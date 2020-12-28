# Advent of Code 2019 - Day 16

# Author:   Rachael Judy
# Date:     12/9/2020
# Purpose:  Compute FFT after 100 iterations (phase 1) and FFT code based on original input offset
#           with repeated pattern after 100 iterations (phase 2)
# Timing:   Takes a little under a minute


import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


def array_to_string(array, delim=' '):
    string = ''
    for x in array:
        string += str(x) + delim
    return string


# get input
og_elements = parseMod.readCSV_single('data/16pattern.csv')
for x in range(len(og_elements)):
    og_elements[x] = int(og_elements[x])
elements = copy.deepcopy(og_elements)
new_elements = [0 for i in range(len(elements))]

# set up working pattern
og_pattern = [0, 1, 0, -1]
new_pattern = []
offset = int(array_to_string(elements[0:7], ''))

# part 1 - brute force
for x in range(100):
    for index in range(len(elements)):
        # expand pattern for index
        for i in range(len(og_pattern)):
            new_pattern.insert(index*i+i, og_pattern[i])

        # iterate through to compute new values
        sum = 0
        for i in range(len(elements)):
            sum += elements[i] * new_pattern[(i+1) % len(new_pattern)]
        elements[index] = abs(sum) % 10

    new_pattern = []  # reset the pattern for next phase

# part 1 summary
code = array_to_string(elements[0:8], '')
print("Part 1: ", code)


# part 2
# expand inputs duplicate 10000
elements = og_elements * 10000
for x in range(100):
    # using knowledge that offset index is in last 600000, all digits that matter correspond to pattern digit 1
    for i in range(len(elements) - 1, len(elements) - 600000, -1):  # work back from end of elements
        elements[i - 1] = (elements[i - 1] + elements[i]) % 10

# part 2 summary
code = array_to_string(elements[offset:offset + 8], '')
print("Part 2: ", code)
