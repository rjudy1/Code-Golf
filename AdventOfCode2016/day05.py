# Advent of Code 2016 Day 5
# Author:   Rachael Judy
# Purpose:  md hash parsing

import hashlib

import parseMod

ready = True
day = 5
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")[0]

passwordA, passwordB, filledB, i, pre = "", ["_"] * 8, 0, 0, data.encode()
while len(passwordA) < 8 or filledB < 8:
    h = hashlib.md5(pre + str(i).encode()).hexdigest()
    if h.startswith("00000"):
        if len(passwordA) < 8:
            passwordA += h[5]
        if h[5].isdigit() and 0 <= (p:=int(h[5])) < 8 and passwordB[p] == "_":
            passwordB[p] = h[6]
            filledB += 1
    i += 1
result = "".join(passwordB) if stage == 'b' else passwordA

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
