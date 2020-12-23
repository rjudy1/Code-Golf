# Advent of Code 2019 - Day 17

# Author:   Rachael Judy
# Date:     12/9/2020
# Purpose:  Use map provided by intcode program to find alignment parameters at intersections and
#           map route through paths to find dust collected value


import os
import sys

import copy
import queue

from intcodecomputer import Computer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# get input
instructions = parseMod.readCSV('data/17robot.csv')
instructions_copy = copy.deepcopy(instructions)  # untouched version for part 2

# part 1
# initialize camera and process
cameras = Computer(instructions)
display = cameras.processInput(queue.SimpleQueue())

array = [[' ' for i in range(53)] for j in range(53)]
# create array from the input string
x, y = 0, 0
for response in display:
    print(chr(response), end='')
    if response == 10:
        x = 0
        y += 1
        continue
    else:
        array[y][x] = chr(response)
        x += 1

# find calibration parameters from array
calibration_sum = 0
# check over array for scaffold on all sides and self is scaffold
for ys in range(1, len(array) - 1):
    for xs in range(1, len(array[0]) - 1):
        if array[ys][xs] != '.' and \
            array[ys-1][xs] == array[ys+1][xs] == array[ys][xs+1] == array[ys][xs-1] == '#':
            calibration_sum += xs * ys

print("Alignment Params Sum: ", calibration_sum)


# part 2
"""
# ASCII function sequence
A # L10, L6, R10 
B # R6, R8, R8, L6, R8
C # L10, R8, R8, L10

L,10, L,6, R,10,   R,6, R,8, R,8, L,6, R,8,   L,10, L,6, R,10,  L,10, R,8, R,8, L,10,   R,6, R,8, R,8, L,6, R,8,   
L,10, R,8, R,8, L,10,   R,6, R,8, R,8, L,6, R,8,   L,10, L,6, R,10,   L,10, R,8, R,8, L,10,   R,6, R,8, R,8, L,6, R,8
"""
# set instructions
instructions_copy[0] = 2
robot = Computer(instructions_copy)

main_routine =['A', ',', 'B', ',', 'A', ',', 'C', ',', 'B', ',', 'C', ',', 'B', ',', 'A', ',', 'C', ',', 'B', '\n']
A = ['L', ',', '1', '0', ',', 'L', ',', '6', ',', 'R', ',', '1', '0', '\n']  # L10, L6, R10
B = ['R', ',', '6', ',', 'R', ',', '8', ',', 'R', ',', '8', ',', 'L', ',', '6', ',', 'R', ',', '8', '\n']
C = ['L', ',', '1', '0', ',', 'R', ',', '8', ',', 'R', ',', '8', ',', 'L', ',', '1', '0', '\n']
vid = ['n', '\n']  # no video, 10 - could process video

# put all in queue
inputQ = queue.SimpleQueue()
for x in main_routine:
    inputQ.put(ord(x))
for a in A:
    inputQ.put(ord(a))
for b in B:
    inputQ.put(ord(b))
for c in C:
    inputQ.put(ord(c))
for v in vid:
    inputQ.put(ord(v))

output = robot.processInput(inputQ)

# ignore all the copies of the map output - could iterate through array and print if yes
# for i in output[:-1]:
#     print(chr(i), end='')

# display final output after all the display code
print("Dust collected: ", output[-1])