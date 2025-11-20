# Advent of Code 2016 Day 4
# Author:   Rachael Judy
# Purpose:  parse most frequent letters, then caesar cipher shift by id

from collections import Counter
import re

import parseMod

ready = True
day = 4
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')

pattern = re.compile(r'((?:[a-z]+-)+)([0-9]+)\[([a-z]{5})\]')
result = 0
for line in data:
    m = pattern.fullmatch(line)
    lc, id, checksum = Counter(sorted(ls:=m.group(1).replace('-', ''))), int(m.group(2)), m.group(3)
    if ''.join(letter for letter, _ in lc.most_common(5)) == checksum:
        result += id
        if stage == 'b' and 'northpole' in ''.join(chr(ord('a') + (ord(l)-ord('a')+id)%26) for l in ls):
            result = id
            break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
