# Advent of Code 2018 - Day 5

# Author:   Rachael Judy
# Date:     12/21/2020
# Purpose:  Reduce a sequence by removing adjacent lowercase and capital identical numbers repetitively, then find
#           the shortest sequence possible by removing all of one letter's occurrences - a bit slow

import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


def react(sequence):
    for i in range(len(sequence)-1, 0, -1):
        if i >= len(sequence): i -= (i%len(sequence)+1)
        if sequence[i].islower() and sequence[i-1].isupper() or sequence[i-1].islower() and sequence[i].isupper():
            if sequence[i].lower() == sequence[i-1].lower():
                sequence.pop(i)
                sequence.pop(i-1)
    return len(sequence)


sequence = parseMod.readCSV_single('data/5reactions.csv')
copy_sequence = copy.deepcopy(sequence)

lowest_remains = 100000
for a in range(ord('A'), ord('Z')+1):
    sequence = copy.deepcopy(copy_sequence)
    for i in range(sequence.count(chr(a).upper())):  # removes the desired chars
        sequence.remove(chr(a).upper())
    for i in range(sequence.count(chr(a).lower())):
        sequence.remove(chr(a).lower())
    lowest_remains = min(lowest_remains, react(sequence))  # keeps minimum remains

print("Part 1 - len remaining: ", react(copy_sequence))
print("Part 2 - minimum sequence len: ", lowest_remains)