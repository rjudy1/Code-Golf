# Advent of Code 2023 Day 23
# Author:   Rachael Judy
# Date:     12/23/23
# Purpose:  DFS traversal of routes with momentum term
# Did I brute force part 2 and just wait until printing slowed? Maybe. Am I going to fix it with graph contraction? Probably later.

import sys
sys.setrecursionlimit(10000)

import numpy as np
import parseMod

ready = True
day = 23
stage = 'b'  # 6390
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


# dfs with step count and slope accounted for
def dfs(pos: int, steps: int, momentum: int = 0, visited: set = set()):
    global data, best, slope_dict
    top = 0
    if int(np.real(pos)) == len(data) - 1:
        if steps > best:  # for waiting out the answer
            best = steps
            print(best)
        return steps
    if momentum != 0:  # momentum forces move
        if data[int(np.real(pos + momentum))][int(np.imag(pos + momentum))] != '#' and pos + momentum not in visited:
            visited.add(pos+momentum)
            top = max(top, dfs(pos+momentum, steps+1, slope_dict[data[int(np.real(pos + momentum))][int(np.imag(pos + momentum))]]))
            visited.discard(pos+momentum)
    else:  # check possible moves
        for dir in [1, -1, 1j, -1j]:
            if data[int(np.real(pos + dir))][int(np.imag(pos + dir))] != '#' and pos + dir not in visited:
                visited.add(pos + dir)
                top = max(top, dfs(pos+dir, steps+1, slope_dict[data[int(np.real(pos + dir))][int(np.imag(pos + dir))]]))
                visited.discard(pos+dir)
    return top  # returning maximum step count


best = 0   # global variable for keeping a display since the actual NP problem doesn't terminate for a while
slope_dict = {'>': 1j, '<': -1j, 'v': 1, '^': -1, '.': 0}
if stage == 'b':
    slope_dict = {'>': 0, '<': 0, 'v': 0, '^': 0, '.': 0}
result = dfs(data[0].ind('.') * 1j, 0)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
