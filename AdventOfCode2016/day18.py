# Advent of Code 2016 Day 18
# Author:   Rachael Judy
# Purpose:  expanding automata

import parseMod

ready = True
day = 18
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')[0]

row = int(data.replace('.', '0').replace('^', '1'), 2)
result = len(data) - row.bit_count()
for _ in range(399999 if stage == 'b' else 39):
    row = ((row << 1) & ((1 << len(data)) - 1)) ^ (row >> 1)
    result += len(data) - row.bit_count()

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
