# Advent of Code 2015 Day 4
# Author:   Rachael Judy
# Purpose:  md5 hash pre+int beginning with 5 and 6 zeros

import hashlib

import parseMod

ready = True
day = 4
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row(f'data/{day:02d}data.csv')[0]

pre = data.encode()
for i in range(1_000_000_000):
    h = hashlib.md5(pre + f'{i}'.encode()).hexdigest()
    if h.startswith('000000' if stage == 'b' else '00000'):
        result = i
        break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
