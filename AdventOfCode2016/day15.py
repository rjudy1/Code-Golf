# Advent of Code 2016 Day 15
# Author:   Rachael Judy
# Purpose:  disc dropping through rotating gaps (chinese remainder theorem again)

from math import gcd

import parseMod

ready = True
day = 15
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv', ' ')
if stage == 'b':
    data.append(f'Disc #{len(data)+1} has 11 positions; at time=0, it is at position 0.'.split())
positions, rems = map(list, zip(*[(int(poss), (-int(start.strip('.')) - int(num.strip('#'))) % int(poss))
                                  for _, num, _, poss, _, _, time, _, _, _, _, start in data]))

def crt(n, a):
    x = m = 1
    for ni, ai in zip(n, a):
        g = gcd(m, ni)
        k = ((ai - x) // g * pow(m // g, -1, ni // g)) % (ni // g)
        x += m * k
        m *= ni // g
    return x % m

result = crt(positions, rems)
print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
