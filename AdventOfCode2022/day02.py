# Advent of Code 2022 Day 2
# Author:   Rachael Judy
# Date:     12/2/22
# Purpose:  Rock, paper, scissors strategy guide options

import parseMod

ready = False
day = 2
stage = 'b'

year = 2022

parseMod.createDataFile(year=year, day=day)
guide = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ' ')

# ord('W') == 87, ord('@') == 64
if stage == 'a':
    result = sum((ord(row[1]) - 22 - ord(row[0])) % 3 * 3 + (ord(row[1]) - ord('W')) for row in guide)
else:
    result = sum((ord(row[1]) - 88) * 3 + (ord(row[1]) - 154 + ord(row[0])) % 3 + 1 for row in guide)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
