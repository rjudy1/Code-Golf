# Advent of Code 2019 - Day 17

# Author:   Rachael Judy
# Date:     12/10/2020
# Purpose:  Some version of SSP - Djikstra/Bellman Ford??

# This is horrendous BFS and Djikstra somehow and I am not here for it right now

import os
import sys

import copy

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

maze = parseMod.readCSV_row('data/18maze.csv')
for row in maze:
    print(row)
print(maze)