# Advent of Code 2017 Day 25
# Author:   Rachael Judy
# Purpose:  process formatted pseudocode for fixed steps

from collections import defaultdict

import parseMod

ready = True
day = 25
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv")

cursor, tape, state, diagnostic_step = 0, defaultdict(int), data[0][0].split()[-1].strip('.'), int(data[0][1].split()[5])
programs = {s[-2]: ((int(w0[-2]), 1 if m0[-3] == 'h' else -1, n0[-2]), (int(w1[-2]), 1 if m1[-3] == 'h' else -1, n1[-2]))
            for s, _, w0, m0, n0, _, w1, m1, n1 in data[1:]}
for step in range(diagnostic_step):
    tape[cursor], cursor, state = (p := programs[state][tape[cursor]])[0], cursor+p[1], p[2]
result = sum(tape.values())

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part='a', day=day, year=year)
