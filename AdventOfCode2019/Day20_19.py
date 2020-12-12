# Advent of Code 2019 - Day 20

# Author:   Rachael Judy
# Date:     12/13/2020
# Purpose:  Compute the least number of steps through the maze
# WORK IN PROGRESS - copied part of 15 logic


import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

import queue  # shouldn't need
import copy

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


# associates Location with each coordinate pair for mapping
class Location:
    def __init__(self, coordinates):
        self.coords = coordinates
        x = coordinates[0]
        y = coordinates[1]
        self.pred = None
        self.direction = [3, 4, 2, 1]
        self.children = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        self.color = 'W'
        self.time = 0


# store time
global time
time = 0
# recursively used for DFS
def DFS_Visit(location, robot, depth):
    global time
    time = time + 1

    # store start time and color the working vertex gray
    location_dict[location].time = time
    location_dict[location].color = 'G'

    inputQ = queue.SimpleQueue()
    # go through adjacencies and store predecessors, follow recursively
    for loca, dire in zip(location_dict[location].children, location_dict[location].direction):
        if location_dict[loca].color == 'W':  # if undiscovered
            # check directions
            inputQ.put(dire)
            output = robot.processInput(inputQ)[0]

            if output == 1 or output == 2:  # if the robot did move, follow that path
                location_dict[loca].pred = location  # save predecessor
                if output == 2:  # save the oxygen location for 1 and the robot state (its position) for part 2
                    global oxygenLocation
                    oxygenLocation = loca
                    global robotCopy
                    robotCopy = copy.deepcopy(robot)
                    global oxDepth
                    oxDepth = depth + 1  # looking at adjacencies of the one in focus so add one

                # search depth
                DFS_Visit(loca, robot, depth+1)

                # back up
                if dire == 1 or dire == 2:
                    inputQ.put(3 - dire)
                elif dire == 3 or dire == 4:
                    inputQ.put(7 - dire)
                robot.processInput(inputQ)

    # color completed vertices
    location_dict[location].color = 'B'

    # record max depth
    global maxDepth
    maxDepth = max(maxDepth, depth)  # depth at bottom

maze = parseMod.readCSV_row('data/20maze.csv')
# turn into graph/dict
# link appropriate sections with edges
# do the same DFS as 15, modded target and movement, account for portals

global location_dict
