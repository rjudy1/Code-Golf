# Advent of Code 2024 Day 6
# Author:   Rachael Judy
# Purpose:  discover path through map with right turns, see where single obstacles create loop, brute force with a path follow optimization

import collections
import copy
import csv
import parseMod

ready = True
day = 6
stage = 'b'
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    map = [row[0] for row in reader]
for i, row in enumerate(map):
    if row.find('^') != -1:
        start = (i,row.find('^'),-1,0)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

node = start
visited_a, ordered_steps = set(), list()
while True:
    x, y, dx, dy = node
    visited_a.add((x, y))
    ordered_steps.append((x,y,dx,dy))
    if not (0 <= x + dx < len(map) and 0 <= y + dy < len(map[0])):
        break
    elif map[x + dx][y + dy] != '#':
        node = (x + dx, y + dy, dx, dy)
    elif map[x + dx][y + dy] == '#':
        node = (x, y, *directions[(1 + directions.index((dx, dy))) % len(directions)])

# part b, check spots along the path to insert an obstacle
counter = 0
for i, j in visited_a:
    if map[i][j] == '#':
        continue
    map[i] = ''.join([map[i][:j], '#', (map[i][(j + 1):] if j < len(map[i]) else '')])

    # start at the node right before the new obstacle
    for k, (x,y,di,dj) in enumerate(ordered_steps):
        if (i,j) == (x,y):
            node = ordered_steps[k-1]
            break

    visited = {node}
    while True:
        x,y,dx,dy = node
        if not (0<=x+dx < len(map) and 0<=y+dy<len(map[0])):  # exited map
            break
        elif map[x + dx][y+dy] != '#':  # clear space
            if (x + dx, y + dy, dx, dy) in visited:
                counter += 1
                break
            node = (x+dx,y+dy,dx,dy)
            visited.add((x + dx,y+dy,dx,dy))
        elif map[x+dx][y+dy] == '#':  # hit obstacle
            if (x,y,*directions[(1+directions.index((dx,dy)))%len(directions)]) in visited:
                counter +=1
                break
            node = (x,y,*directions[(1+directions.index((dx,dy)))%len(directions)])
            visited.add((x,y,*directions[(1+directions.index((dx,dy)))%len(directions)]))
    map[i] = ''.join([map[i][:j], '.', (map[i][(j + 1):] if j < len(map[i]) else '')])  # reset map

if stage == 'a':
    result = len(visited_a)
else:
    result = counter

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
