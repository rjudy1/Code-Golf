# Advent of Code 2020 - Day 9

# Author:   Rachael Judy
# Date:     12/9/2020
# Purpose:  Find number in which previous 25 does not possess two numbers to sum to it
#           Find contiguous set in whole list that does sum to the number and add its min and max


import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


# input numbers
numbers = parseMod.readCSV('data/9numbers.csv', '\n')

# initial preamble
preamble = numbers[0:25]
# part 1 - find number that previous 25 can't sum to
for to_match in numbers[25:]:  # look for number that cannot be summed from the preamble
    match = False
    for x in range(len(preamble)):  # check every number in preamble
        for y in range(len(preamble)):
            if x != y and preamble[x] + preamble[y] == to_match:
                match = True
                break
        if match:
            break
    # if no match was found in that preamble, display the secret number
    if not match:
        print("Mismatch: ", to_match)
        break

    # shift the preamble
    preamble.pop(0)
    preamble.append(to_match)


# part 2 - find contiguous subset to sum to toMatch
subset_found = False
start_index, end_index = 0, 0
for i in range(len(numbers)):
    sum = numbers[i]
    start_index = i
    for j in range(i+1, len(numbers)):
        sum += numbers[j]
        if sum == to_match:
            end_index = j  # inclusive
            subset_found = True
            break
        elif sum >= to_match:
            break
    if subset_found:
        break

# show sum of min and max in set
minimum = min(numbers[start_index:end_index+1])
maximum = max(numbers[start_index:end_index+1])
print("Sum of min and max: ", minimum + maximum)
