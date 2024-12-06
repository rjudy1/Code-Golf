# Advent of Code 2024 Day 6
# Author:   Rachael Judy
# Purpose:
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

counter = 0
visited_2 = set()

# node = start
# if stage == 'a' and (i,j) != (node[0],node[1]):
#     continue
# elif stage == 'b':
#     if (i, j) == node[0:2]:
#         continue
#     map[i] = map[i][:j] + '#' + (map[i][(j + 1):] if j < len(map[i]) else '')

# visited = {node}
# queue = collections.deque([node])
# directions = [(-1,0), (0, 1), (1, 0), (0,-1)]
# while queue:
#     x,y,dx,dy = queue.popleft()
#     visited_2.add((x,y))
#     if not (0<=x+dx < len(map) and 0<=y+dy<len(map[0])):
#         break
#
#     if map[x + dx][y+dy] != '#':
#
#         if (x,y,*directions[(1+directions.index((dx,dy)))%len(directions)]) in visited:
#             counter+=1
#         node = (x+dx,y+dy,dx,dy)
#         visited.add((x + dx,y+dy,dx,dy))
#     elif map[x+dx][y+dy] == '#':
#         node = (x,y,*directions[(1+directions.index((dx,dy)))%len(directions)])
#         visited.add((x,y,*directions[(1+directions.index((dx,dy)))%len(directions)]))


for i in range(len(map)):
    for j in range(len(map)):
        new_map=copy.deepcopy(map)
        node = start
        if stage == 'a' and (i,j) != (node[0],node[1]):
            continue
        elif stage == 'b':
            if (i, j) == node[0:2]:
                continue
            map[i] = map[i][:j] + '#' + (map[i][(j + 1):] if j < len(map[i]) else '')

        visited = {node}
        directions = [(-1,0), (0, 1), (1, 0), (0,-1)]
        while True:
            x,y,dx,dy = node
            visited_2.add((x,y))
            if not (0<=x+dx < len(map) and 0<=y+dy<len(map[0])):
                break

            if map[x + dx][y+dy] != '#':
                if (x + dx, y + dy, dx, dy) in visited:
                    print(i, j)
                    counter += 1
                    break
                node = (x+dx,y+dy,dx,dy)
                visited.add((x + dx,y+dy,dx,dy))

            elif map[x+dx][y+dy] == '#':
                if (x,y,*directions[(1+directions.index((dx,dy)))%len(directions)]) in visited:
                    print(i, j)
                    counter +=1
                    break
                node = (x,y,*directions[(1+directions.index((dx,dy)))%len(directions)])
                visited.add((x,y,*directions[(1+directions.index((dx,dy)))%len(directions)]))
        map = copy.deepcopy(new_map)

if stage == 'a':
    result = len(visited_2)
else:
    result = counter



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
