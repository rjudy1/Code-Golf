# Advent of Code 2015 Day 10
# Author:   Rachael Judy
# Purpose:  look and say sequence

import itertools

import parseMod

ready = True
day = 10
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')[0]

for _ in range(40 if stage=='a' else 50):
    data = ''.join(f"{len(list(group))}{digit}" for digit, group in itertools.groupby(data))
result = len(data)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
