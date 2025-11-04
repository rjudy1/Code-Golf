# Advent of Code 2017 Day 9
# Author:   Rachael Judy
# Purpose:  parser state machine to count garbage and score group depth

import parseMod

ready = False
day = 9
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_single("data/" + str(day).zfill(2) + "data.csv")

depth = score = garbage = 0
in_gar = in_cancel = False
for ch in iter(data):
    if in_cancel: in_cancel = False             # comma in group or at a cancelled character
    elif ch == '!': in_cancel = True            # in cancellation
    elif in_gar:                                # in garbage
        if ch == '>': in_gar = False            # end of garbage, not cancelled
        else: garbage += 1                      # garbage count
    elif ch == '<': in_gar = True               # start of garbage
    elif ch == '{': depth += 1; score += depth  # start of group
    elif ch == '}': depth -= 1                  # end of group
result = score if stage == 'a' else garbage

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
