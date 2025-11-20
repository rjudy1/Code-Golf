# Advent of Code 2015 Day 5
# Author:   Rachael Judy
# Purpose:  match strings to certain rules

import re

import parseMod

ready = True
day = 5
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')

result = sum(1 for ln in data if re.match(re.compile(r'^(?!.*(?:ab|cd|pq|xy))(?=(?:.*[aeiou]){3,})(?=.*([a-z])\1)[a-z]*$' if stage == 'a' else r'^(?=.*([a-z]{2}).*\1)(?=.*([a-z]).\2)[a-z]*$'), ln))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
