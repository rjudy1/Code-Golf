# Advent of Code 2022 Day 3
# Author:   Rachael Judy
# Date:     12/3/22
# Purpose:  Set intersection within row and between three rows

import parseMod

ready = False
day = 4
stage = 'a'

year = 2022

parseMod.createDataFile(year=year, day=day)
rucksacks = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

# ord(a)=97 -> 1, ord(A)=65 -> 26

if stage == 'a':
    pass
else:
    pass
if not ready:
    print(f'result: \n{score}')
elif ready:
    print("SUBMITTING RESULT: ", score)
    parseMod.submit(score, part=stage, day=day, year=year)
