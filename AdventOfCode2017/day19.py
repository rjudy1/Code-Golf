# Advent of Code 2017 Day 19
# Author:   Rachael Judy
# Purpose:  follow the graphic path

import parseMod

ready = False
day = 19
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

p, d, l, c = data[0].index('|') + 0j, 1j, [], 0
while (ch := data[int(p.imag)][int(p.real)]) != ' ':
    if ch == '+':
        d *= next(k for k in [1j, -1j] if data[int((p + k * d).imag)][int((p + k * d).real)] != ' ')
    elif ch.isalpha():
        l.append(ch)
    p += d
    c += 1
result = ''.join(l) if stage == 'a' else c

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
