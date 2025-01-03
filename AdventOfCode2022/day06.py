# Advent of Code 2022 Day 6
# Author:   Rachael Judy
# Date:     12/6/22
# Purpose:  shifting window of unique characters

import parseMod

stage = 'b'
day = 6
year = 2022

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


def find_start(string, size):
    for i in range(size-1, len(data[0])):
        if len(set(string[i-size+1:i+1])) == size:
            return i


if stage == 'a':
    result = find_start(data[0], 4)+1
else:
    result = find_start(data[0], 14)+1

print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
