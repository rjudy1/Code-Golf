# Advent of Code 2016 Day 9
# Author:   Rachael Judy
# Purpose:  recursive expansion of compressed repetitions in string

from functools import lru_cache
import re

import parseMod

ready = True
day = 9
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')[0]
patt = re.compile(r'\((\d+)x(\d+)\)')

@lru_cache
def decompress(s, recurse=False):
    ret = 0
    while m := patt.search(s):
        (_, end), (size, reps) = m.span(), map(int, m.groups())
        ret += m.regs[0][0] + (len(s[end:end+size]) if not recurse else decompress(s[end:end+size], recurse)) * reps
        s = s[end+size:]
    return ret + len(s)

result = decompress(data, stage=='b')

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
