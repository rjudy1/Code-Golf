# Advent of Code 2016 Day 6
# Author:   Rachael Judy
# Purpose:  most and least common value in columns

from collections import Counter, defaultdict

import parseMod

ready = True
day = 6
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')

result = ''.join((lambda cols: [Counter(c).most_common()[-1 if stage=='b' else 0][0] for c in cols])(zip(*data)))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
