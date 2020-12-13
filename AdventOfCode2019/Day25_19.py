# Advent of Code 2019 - Day 25

# Author:   Rachael Judy
# Date:     12/13/2020
# Purpose:


import os
import sys

import queue  # shouldn't need?
import copy

from intcodecomputer import Computer

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

instructions = parseMod.readCSV('data/25robot.csv')

input_q = queue.SimpleQueue()
droid = Computer(instructions)
