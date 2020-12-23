# Advent of Code 2020 - Day 6

# Author:   Rachael Judy
# Date:     12/6/2020
# Purpose:  Survey questions answered by each group (like an engagement survey)
#               AND and OR versions

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

answers = parseMod.readCSV_batch('data/6answers.csv')

sumOr = 0
sumAnd = 0
for group in answers:
    # phase 1
    set = []
    for letter in group:
        if letter not in set and letter != ' ':
            sumOr += 1
            set.append(letter)

    # phase 2 - look across all
    persons = group.strip().split(' ')
    for letter in persons[0]:
        answeredYes = True  # yes by all
        for i in range(len(persons)):  # check for all answering that one
            if letter not in persons[i]:
                answeredYes = False
        if answeredYes:
            sumAnd += 1

print("Or Answers ", sumOr)
print("And Answers ", sumAnd)