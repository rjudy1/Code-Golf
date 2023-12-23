# Advent of Code 2023 Day 21
# Author:   Rachael Judy
# Date:     12/21/23
# Purpose:  Find positions possible at exact number of steps, then with infinite grid

from collections import deque
import parseMod

ready = False
day = 21
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

for r, row in enumerate(data):
    if 'S' in row:
        S = (r, row.index('S'))

steps_available = 26501365
visited = {S}
final_spots = 0
queue = deque([(*S, 0)])

# steps_available = 64
# while queue:
#     r, c, step = queue.popleft()
#     if (steps_available - step) % 2 == 0:
#         final_spots += 1
#     for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         if 0 <= r+dr < len(data) and 0 <= c+dc < len(data[0]) and (data[r+dr][c+dc] == '.' or data[r+dr][c+dc] == 'S') \
#                 and (r+dr, c+dc) not in visited and step < steps_available:
#             queue.append((r+dr, c+dc, step+1))
#             visited.add((r+dr, c+dc))

# cache distance from four corners, midpoints, and start location
def bfs(start):
    global data
    visited = {start}
    pos_to_step = dict()
    queue = deque([(*start, 0)])
    while queue:
        r, c, step = queue.popleft()
        pos_to_step[(r, c)] = step
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= r+dr < len(data) and 0 <= c+dc < len(data[0]) and (r+dr, c+dc) not in visited\
                    and (data[(r+dr)][(c+dc)] == '.' or data[(r+dr) % len(data)][(c+dc) % len(data[0])] == 'S'):
                queue.append((r+dr, c+dc, step+1))
                visited.add((r+dr, c+dc))
    return pos_to_step

def manhattan(a, b):
    return abs(a[1]-b[1] + a[0]-b[0])

# distances = dict()
# for start_pos in [S, (S[0], 0), (S[0], len(data[0])-1), (0, 0), (0, len(data[0])-1), (0, S[1]), (len(data)-1, S[1]), (len(data)-1, 0), (len(data)-1, len(data[0])-1)]:
#     distances[start_pos] = bfs(start_pos)
# # just walk along vertical and diagonal until hit the desired tile and then
# # iterate giant rectangle from position S - steps_available / len map to S +
# final_spots = 0
# for i in range(-steps_available//len(data) - 1, steps_available//len(data) + 2):
#     for j in range(-steps_available // len(data[0]) - 1, steps_available // len(data[0]) + 2):
#         # for this rectangle, find the closest position
#         if i < 0 and j < 0:  # went up and left
#             closest = (len(data)-1, len(data[0]) - 1)
#             increment = 2
#         elif i > 0 and j < 0:  # down and left
#             closest = (0, len(data[0])-1)
#             increment = 2
#         elif i < 0 and j > 0:  # up and right
#             closest = (len(data)-1, 0)
#             increment = 2
#         elif i > 0 and j > 0:  # down and right
#             closest = (0, 0)
#             increment = 1
#         elif i == 0 and j > 0: # right
#             closest = (S[0], 0)
#             increment = 1
#         elif i == 0 and j < 0: # left
#             closest = (S[0], len(data[0])-1)
#             increment = 1
#         elif i < 0 and j == 0:  # up
#             closest = (len(data)-1, S[1])
#             increment = 1
#         elif i > 0 and j == 0: # down
#             closest = (0, S[1])
#             increment = 1
#         else:
#             closest = S
#             increment = 0
#         # distance from S to closest position + distance to squares in range <= available steps
#         # i*len(data), j*len(data[0]) - (closest-position)
#         distance = manhattan((i*len(data), j*len(data[0])), (0, 0)) - manhattan(closest, S) + increment
#         if distance < steps_available:
#             for position in distances[closest]:
#                 if (steps_available - (distance + distances[closest][position])) % 2 == 0:
#                     final_spots += 1


# 22201698
if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
