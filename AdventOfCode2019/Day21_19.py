# Advent of Code 2019 - Day 21

# Author:   Rachael Judy
# Date:     12/11/2020
# Purpose:  Create springcode program that tells robot when to jump based on sight in front of it

import os
import sys

import queue

from intcodecomputer import Computer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# set part
part = 2

instructions = parseMod.readCSV('data/21jumper.csv')
jumper = Computer(instructions)

# part 1 pattern - (!A+!B+!C)D - prevents always jump if can for some reason, otherwise preemptive jump
if part == 1:
    springcode = "NOT B T\nNOT C J\nOR T J\nAND D J\nNOT A T\nOR T J\nWALK\n"  # part 1

# part 2 pattern, similar logic but if gap H ahead, don't know if E will be problem so get closer to see
# - possible missing case
else:
    springcode = "NOT B T\nNOT C J\nOR T J\nAND D J\nAND H J\nNOT A T\nOR T J\nRUN\n"  # part 2

# run through jumped robot
inputQ = queue.SimpleQueue()
for letter in springcode:
    inputQ.put(ord(letter))

# process and display output
answer = jumper.processInput(inputQ)
for x in answer[:-1]:
    print(chr(x), end='')
print("RESULT: ", answer[-1])
