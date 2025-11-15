# Advent of Code 2017 Day 24
# Author:   Rachael Judy
# Purpose:  build highest strength bridge with two sided nodes (dfs could use some caching/pruning)

import parseMod

ready = True
day = 24
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", '/')


def dfs(open_port, unused, strength, length):
    global top_strength, top_length_strength_pair
    top_strength = max(top_strength, strength)  # keep best strength
    top_length_strength_pair = max((length, strength), top_length_strength_pair)  # best length, tie broken by strength

    for i, (a, b) in enumerate(unused):
        if a == open_port or b == open_port:  # check possible matches
            dfs(b if a == open_port else a, unused[:i] + unused[i+1:], strength + a + b, length + 1)
top_strength, top_length_strength_pair = 0, (0, 0)  # strength, (length, strength)
dfs(0, [list(map(int, c)) for c in data], 0, 0)
result = top_strength if stage == 'a' else top_length_strength_pair[1]

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
