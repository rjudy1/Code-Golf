# Advent of Code 2023 Day 9
# Author:   Rachael Judy
# Date:     12/9/23
# Purpose:  propagate difference of each line of values until line of zeroes, then backpropagate from end and beginning


import parseMod

ready = True
day = 9
stage = 'a'
year = 2023

parseMod.createDataFile(year=year, day=day)
array = [[int(num) for num in a] for a in parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")]

result = 0
for row in array:
    row_history = [row.copy()]
    while row_history[-1].count(0) != len(row_history[-1]):  # add lines to history until all zeroes
        row_history.append([row_history[-1][i + 1] - row_history[-1][i] for i in range(len(row_history[-1])-1)])
    row_history[-1].append(0)

    if stage == 'a':  # extrapolate from end of history
        for r in range(len(row_history) - 2, -1, -1):
            row_history[r].append(row_history[r][-1] + row_history[r + 1][-1])
        result += row_history[0][-1]
    elif stage == 'b':  # extrapolate from beginning of history
        for r in range(len(row_history) - 2, -1, -1):
            row_history[r].insert(0, row_history[r][0] - row_history[r + 1][0])
        result += row_history[0][0]

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
