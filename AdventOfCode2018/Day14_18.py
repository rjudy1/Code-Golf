# Advent of Code 2018 - Day 14

# Author:   Rachael Judy
# Date:     12/24/2020
# Purpose:  Generate an extended string of scores (scores are single digits of sum of two elves - first one go to 50000
#           second has to be extended to take forever (around a minute) - short code tho

recipes = '430971'  # your input here

score = '37'  # initial scores, extend off here
pelf1, pelf2 = 0, 1  # position elfs
while recipes not in score[-7:]:
    score += str(int(score[pelf1]) + int(score[pelf2]))  # new recipe(s) generated
    pelf1 = (pelf1 + int(score[pelf1]) + 1) % len(score)  # position in array elf1
    pelf2 = (pelf2 + int(score[pelf2]) + 1) % len(score)  # position in array elf2

print('Part 1:', score[int(recipes):int(recipes)+10])
print('Part 2:', score.index(recipes))
