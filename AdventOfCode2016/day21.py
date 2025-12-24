# Advent of Code 2016 Day 21
# Author:   Rachael Judy
# Purpose:  scrambling and unscrambling operations on string

import re

import parseMod

ready = True
day = 21
stage = 'a'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')

s = list('abcdefgh' if stage == 'a' else 'fbgdceah')
for ln in data if stage == 'a' else reversed(data):
    if m := re.match(r'swap position (\d+) with position (\d+)', ln):
        i, j = map(int, m.groups())
        s[i], s[j] = s[j], s[i]
    elif m := re.match(r'swap letter (.) with letter (.)', ln):
        i, j = map(s.index, m.groups())
        s[i], s[j] = s[j], s[i]
    elif m := re.match(r'rotate (left|right) (\d+)', ln):
        k = int(m.group(2)) * (-1 if m.group(1) == 'left' else 1) * (-1 if stage == 'b' else 1) % len(s)
        s = s[-k:] + s[:-k]
    elif m := re.match(r'rotate based on position of letter (.)', ln):
        if stage == 'a':
            i = s.index(m.group(1))
            k = (1 + i + (i >= 4)) % len(s)
        else:
            new = s.index(m.group(1))
            for i in range(len(s)):  # could closed-form it as it's O(len(s))
                if (i + 1 + i + (i >= 4)) % len(s) == new:
                    k = -(1 + i + (i >= 4)) % len(s)
        s = s[-k:] + s[:-k]
    elif m := re.match(r'reverse positions (\d+) through (\d+)', ln):
        i, j = map(int, m.groups())
        s[i:j+1] = reversed(s[i:j+1])
    elif m := re.match(r'move position (\d+) to position (\d+)', ln):
        i, j = map(int, m.groups()) if stage == 'a' else reversed([*map(int, m.groups())])
        c = s.pop(i)
        s.insert(j, c)

result = ''.join(s)
print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
