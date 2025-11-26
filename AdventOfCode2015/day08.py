# Advent of Code 2015 Day 8
# Author:   Rachael Judy
# Purpose:  match and compact/encode escape sequences

import re

import parseMod

ready = True  # 1371,2117
day = 8
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
with (open(f'data/{day:02d}data.csv') as f):
    p = re.compile(r'\\\\|\\"|\\x[0-9a-fA-F]{2}')
    result = sum(2 + (sum(1 if m.group() in ('\\\\', '\\"') else 3 for m in p.finditer(ln)) if stage == 'a'
                      else ln.count('\\') + ln.count('"')) for ln in f)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
