# Advent of Code 2020 - Day 12

# Author:   Rachael Judy
# Date:     12/12/2020
# Purpose:  Find Manhattan distance to ship with ship based directions and waypoint based directions


import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# get directions
directions = parseMod.readCSV_row('data/12directions.csv', '\n')

# part 1
position = [0, 0]
orientation = 1  # start east - 0, 1, 2, 3 == N, E, S, W
for dir in directions:
    # set absolute position
    position[0] += int(dir[1:]) * ((dir[0] == 'E') - (dir[0] == 'W'))
    position[1] += int(dir[1:]) * ((dir[0] == 'N') - (dir[0] == 'S'))

    # set orientation
    for i in range(int(int(dir[1:])/90)):
        orientation = (orientation + ((dir[0] == 'R') - (dir[0] == 'L'))) % 4

    # move in orientation
    position[1] += int(dir[1:]) * ((orientation == 0) - (orientation == 2)) * (dir[0]=='F')
    position[0] += int(dir[1:]) * ((orientation == 1) - (orientation == 3)) * (dir[0]=='F') # east west

print("PART 1: ", abs(position[0]) + abs(position[1]))


# part 2
waypoint = [10, 1]  # position is relative to ship at all times
position = [0, 0]
for dir in directions:
    # set waypoint absolute pos
    waypoint[0] += int(dir[1:]) * ((dir[0] == 'E') - (dir[0] == 'W'))
    waypoint[1] += int(dir[1:]) * ((dir[0] == 'N') - (dir[0] == 'S'))

    # a bit annoyed with the quality of these ifs
    if dir[0] == 'R':
        # rotate clockwise
        for i in range(int(int(dir[1:])/90)):
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]

    elif dir[0] == 'L':
        # rotate counterclockwise
        for i in range(int(int(dir[1:])/90)):
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]

    # move ship and waypoints accordingly
    elif dir[0] == 'F':
        # get new positions
        position[0] += int(dir[1:]) * (waypoint[0])
        position[1] += int(dir[1:]) * (waypoint[1])

print("PART 2: ", abs(position[0]) + abs(position[1]))
