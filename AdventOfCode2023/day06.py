# Advent of Code 2023 Day 6
# Author:   Rachael Judy
# Date:     12/6/23
# Purpose:

import parseMod

ready = True
day = 5
stage = 'b'

year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_batch("data/" + str(day).zfill(2) + "data.csv", delim='\n')



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
