# Advent of Code 2024 Day 15
# Author:   Rachael Judy
# Purpose:  lanternfish again

import csv
import parseMod

ready = True
day = 15
stage = 'a'
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    # TODO: parse the input into walls, boxes, robot
    map = [row[0] for row in reader][0]
    # TODO add walls around border, find max and min positions

walls = set()
boxes = set()
robot = complex(0,0)
instructions = list()
directions = {'>': 1j, '^': -1, '<': -1j, 'v': 1}

for instr in instructions:
    # try to move robot in direction, add wall check
    # check blocks in this direction
    pos = robot
    while 0 <= pos.real < len(board) and 0 <= pos.imag <= len(board[0]):
        pos += directions[instr]
        relevant_boxes = set()
        if pos in boxes:
            relevant_boxes.add(pos)
        elif pos in walls:
            # can't move, don't update position
            break
        else:
            for box in relevant_boxes:
                boxes.remove(box)
                boxes.add(pos + directions[instr]) # this is going to create an overlap orblem,need a dict
            # move allowed
            robot = pos
            break

result = sum(box.real*100+box.imag for box in boxes)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
