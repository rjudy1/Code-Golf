# Advent of Code 2016 Day 7
# Author:   Rachael Judy
# Purpose:  match abba not in square brackets and aba/[bab] pairs

import numpy as np
import re

import parseMod

ready = False
day = 7  # 105, 258
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')

result = np.count_nonzero([re.search(r"(.)(?!\1)(.)\2\1", line) and not re.search(r"\[[^]]*(.)(?!\1)(.)\2\1", line) for line in data])
if stage == 'b':
    aba = re.compile(r'(?=(.)(.)\1)')
    result = sum(bool(
        {a + b + a for segment in re.split(r'\[.*?\]', line) for a, b in aba.findall(segment) if a != b} & {b + a + b for segment in re.findall(r'\[(.*?)\]', line) for a, b in aba.findall(segment) if a != b})
                 for line in data)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
