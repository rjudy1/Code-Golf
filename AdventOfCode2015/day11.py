# Advent of Code 2015 Day 11
# Author:   Rachael Judy
# Purpose:  incrementing alphabetic strings

import parseMod

ready = True
day = 11
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')[0]

def inc(d):
    for i in range(len(d)-1, -1, -1):
        d[i] = (d[i] + 1) % 26
        if d[i] != 0:
            break

def has_two_pairs(d):
    pairs = set()
    i = 0
    while i < len(d)-1:
        if d[i] == d[i+1]:
            pairs.add(d[i])
            i += 2
        else:
            i += 1
    return len(pairs) >= 2

def next_pass(s):
    d = [ord(c) - 97 for c in s]
    inc(d)
    while not (any(d[i] + 1 == d[i+1] == d[i+2] - 1 for i in range(len(d)-2)) and not any(x in (8, 11, 14) for x in d) and has_two_pairs(d)):
        inc(d)
    return ''.join(chr(x + 97) for x in d)

result = next_pass(data) if stage == 'a' else next_pass(next_pass(data))

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
