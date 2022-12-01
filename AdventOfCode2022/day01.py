# Advent of Code 2022 Day 1
# Author:   Rachael Judy
# Date:     12/1/22
# Purpose:  Split a data file twice and find the top 3 sums of each batch

import parseMod

ready = False
day = 1
stage = 'a'

year = 2022

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_batch("data/" + str(day).zfill(2) + "data.csv")
calories = [[int(x) for x in arr.rstrip().split(' ')] for arr in array]

maxCals = []
for elf in calories:
    maxCals.append(sum(elf))

maxCals.sort()
if stage == 'a':
    result = maxCals[-1]
else:
    result = maxCals[-1] + maxCals[-2] + maxCals[-3]

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
