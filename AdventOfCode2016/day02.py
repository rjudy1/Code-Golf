# Advent of Code 2016 Day 2
# Author:   Rachael Judy
# Purpose:  follow step directions within bounds of a keypad

from functools import reduce

import parseMod

ready = True
day = 2
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')

pk_map = {-1 - 1j: '1', -1: '2', -1 + 1j: '3', -1j: '4', 0: '5', 1j: '6', 1 - 1j: '7', 1: '8', 1 + 1j: '9'} if stage == 'a' \
    else {-2: '1', -1-1j: '2', -1: '3', -1+1j: '4', -2j: '5', -1j: '6', 0: '7', 1j: '8', 2j: '9', 1-1j: 'A', 1: 'B', 1+1j: 'C', 2: 'D'}
pd_map = {'D': 1, 'L': -1j, 'R': 1j, 'U': -1}
pos = 0 if stage == 'a' else -2j
result = ''.join(pk_map[reduce(lambda p, s: newp if (newp := p + pd_map[s]) in pk_map else p, line, pos)] for line in data)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
