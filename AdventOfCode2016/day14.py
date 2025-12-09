# Advent of Code 2016 Day 14
# Author:   Rachael Judy
# Purpose:  64th index such that md5 hash of salt+index contains a triple then a quintuple in the next 1000 hashes

from functools import cache
import hashlib
import re

import parseMod

ready = True
day = 14
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
salt = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')[0]

@cache
def hash(i: int, salt: str, stretch: bool) -> str:
    h = hashlib.md5(f"{salt}{i}".encode('utf-8')).hexdigest()
    for _ in range(2016*stretch):
        h = hashlib.md5(h.encode('utf-8')).hexdigest()
    return h

found, result = 0, 0
while found < 64:
    if m := re.search(r'(.)\1\1', hash(result := result+1, salt, stage == 'b')):
        found += (sum(m.group(1)*5 in hash(result+1+j, salt, stage == 'b') for j in range(1000)) != 0)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
