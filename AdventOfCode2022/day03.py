# Advent of Code 2022 Day 3
# Author:   Rachael Judy
# Date:     12/3/22
# Purpose:  Set intersection within row and between three rows

import parseMod

ready = False
day = 3
stage = 'a'

year = 2022

parseMod.createDataFile(year=year, day=day)
rucksacks = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

# ord(a)=97 -> 1, ord(A)=65 -> 26
get_score = lambda ch: ord(ch) - 38 if ord(ch) < ord('a') else ord(ch) - 96

if stage == 'a':
    score = sum(get_score((set(r[:len(r) // 2]) & set(r[len(r) // 2:])).pop()) for r in rucksacks)
else:
    score = sum(get_score(set.intersection(*map(set, rucksacks[i:i+3])).pop()) for i in range(0, len(rucksacks), 3))

if not ready:
    print(f'result: \n{score}')
elif ready:
    print("SUBMITTING RESULT: ", score)
    parseMod.submit(score, part=stage, day=day, year=year)
