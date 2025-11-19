# Advent of Code 2015 Day 1
# Author:   Rachael Judy
# Purpose:  follow floor move instructions

import parseMod

ready = True
day = 1
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")[0]

result = data.count('(') - data.count(')')
if stage == 'b':
    pos = 0
    for i, c in enumerate(data):
        pos += 1 if c == '(' else -1
        if pos == -1:
            result = i+1
            break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
