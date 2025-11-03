# Advent of Code 2017 Day 7
# Author:   Rachael Judy
# Purpose:

import parseMod

ready = True
day = 7
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSVInts("data/" + str(day).zfill(2) + "data.csv", delim='\t')



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
