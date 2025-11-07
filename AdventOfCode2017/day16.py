# Advent of Code 2017 Day 16
# Author:   Rachael Judy
# Purpose:  letters move in patterns, cycle detection

import parseMod

ready = True
day = 16
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ',')[0]

programs = [chr(i) for i in range(ord('a'), ord('p')+1)]
first_order, iter = '', 0
while iter < 1_000_000_000:
    for instr in data:
        if instr[0] == 's':
            programs = programs[-int(instr[1:]):] + programs[:-int(instr[1:])]
        elif instr[0] == 'x':
            a, b = map(int, instr[1:].split('/'))
            programs[a], programs[b] = programs[b], programs[a]
        elif instr[0] == 'p':
            a, b = instr[1:].split('/')
            ai, bi = programs.index(a), programs.index(b)
            programs[ai], programs[bi] = b, a
    result = ''.join(programs)
    if not iter:
        first_order = result
    elif result == first_order:  # instead of storing all the cycle elements, repeats time to generate part of cycle
        iter = 1_000_000_000 - 1_000_000_000 % iter
    iter += 1
result = first_order if stage == 'a' else result

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
