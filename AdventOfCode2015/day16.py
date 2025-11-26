# Advent of Code 2015 Day 16
# Author:   Rachael Judy
# Purpose:  find match to template characteristics

import operator as op

import parseMod

ready = False
day = 16
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv')

template = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
cmp = {'cats': op.gt, 'trees': op.gt, 'pomeranians': op.lt, 'goldfish': op.lt} if stage == 'b' else {}
for sm1, l in enumerate(data):  # find sue matching template ie if sue i is a subset of template
    if all(cmp.get(f:=l[i].strip(':'), op.eq)(int(l[i+1].strip(',')), template[f]) for i in range(2, len(l), 2)):
        result = sm1 + 1
        break

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
