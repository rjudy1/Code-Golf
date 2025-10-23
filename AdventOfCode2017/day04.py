# Advent of Code 2017 Day 4
# Author:   Rachael Judy
# Purpose:  validate duplicate words/anagrams in passphrase

import parseMod

ready = True
day = 4
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv", delim='\t')

result = sum(len((s := r.split())) == len({*s} if stage == 'a' else {''.join(sorted(w)) for w in s}) for r in data)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
