# Advent of Code 2016 Day 23
# Author:   Rachael Judy
# Purpose:  basic cpu + toggle instruction + reverse engineer the assembly

import math

import parseMod

ready = True
day = 23
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv', ' ')
result = math.factorial(7 if stage == 'a' else 12) + int(data[19][1]) * int(data[20][1])

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
