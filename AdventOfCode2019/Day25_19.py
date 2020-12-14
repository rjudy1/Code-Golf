# Advent of Code 2019 - Day 25

# Author:   Rachael Judy
# Date:     12/13/2020
# Purpose:  Final advent of code - explore ship and find checkpoint - store password
# Solution: keep easter egg, astronaut ice cream, mutex, and tambourine - don't take magnet, escape pod, photons, lava
# my Map:
#  nav (peas) ----------- breach -------- storage
#                           |
#                    gift center   ---------- holodeck --------------- fountain (ic) -------- stable -------- corridor
#                    (photons x)                  |                           |             (ornament)
#                                             passages -- warp -- sickbay  engineering
#                                          (escape pod x)                      (tambourine)
#                                                 |
#                                  arcade ------ lab --- obs
#                               (magnet x)    (lava x)
#                                    |
#  cockpit(locked) -- security -- kitchen
#

import os
import sys

import queue

from intcodecomputer import Computer

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# get ship instructions
instructions = parseMod.readCSV('data/25robot.csv')

# set up queue and create droid
input_q = queue.SimpleQueue()
droid = Computer(instructions)

# run program
while True:
    # display output
    message = droid.processInput(input_q)
    for letter in message:
        print(chr(letter), end='')

    # get input and send to droid
    entry = input()
    for letter in entry:
        input_q.put(ord(letter))
    input_q.put(ord('\n'))
