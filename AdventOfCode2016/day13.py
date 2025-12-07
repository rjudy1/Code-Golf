# Advent of Code 2016 Day 13
# Author:   Rachael Judy
# Purpose:

import parseMod

ready = True
day = 13
stage = 'a'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv', ' ')




print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
