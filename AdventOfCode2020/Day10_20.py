# Advent of Code 2020 - Day 10

# Author:   Rachael Judy
# Date:     12/10/2020
# Purpose:  Find product of count voltage diff between each element in adapters - no duplicates
#           Find total number of adapter arrangements that meet conditions
#           Part 2 works if can remove max of three adapters in a row

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# get adapters
adapters = parseMod.readCSV('data/10adapters.csv', '\n')
adapters.sort()  # must go up, no duplicates
print("Adapter Jolts: ", adapters)

adapters.insert(0, 0)  # insert source
adapters.append(adapters[-1] + 3)  # insert device

# part 1
# compute differences between each adapter in the list
differences = [0, 0, 0, 0]  # create difference array
for i in range(1, len(adapters)):
    differences[adapters[i] - adapters[i-1]] += 1

print("Diff array: ", differences)
print("Part 1: ", differences[1] * differences[3])

# part 2
# save possibilities to be removed that maintain the validity of the arrangement
possibilities = []
for i in range(1, len(adapters) - 1):
    if adapters[i+1] - adapters[i - 1] <= 3:
        possibilities.append((adapters[i]))
print("Possiblities: ", possibilities)

# count how many triples occur - based on pattern there are no quadruples or more in sequence
triple_count = 0
for p in range(len(possibilities)-2):
    if possibilities[p+2] - possibilities[p] == 2:
        triple_count += 1

# compute possibilities =
# 2^number_of_nontriples (include or not) * 7^number_of_triples (opt for sequential three removable, exclude none)
arrangements = 2**(len(possibilities)-triple_count*3) * (7**triple_count)
print("Part 2 Arrangements: ", arrangements)
