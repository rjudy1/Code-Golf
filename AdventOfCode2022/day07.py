# Advent of Code 2022 Day 7
# Author:   Rachael Judy
# Date:     12/7/22
# Purpose:

import parseMod

stage = 'b'
day = 7
year = 2022

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")



if stage == 'a':
    result = find_start(data[0], 4)+1
else:
    result = find_start(data[0], 14)+1

print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
