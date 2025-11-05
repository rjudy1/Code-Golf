# Advent of Code 2019 - Day 23

# Author:   Rachael Judy
# Date:     12/12/2020
# Purpose:  Run intcode program on fifty network computers communicating
#

import copy
import os
import sys
import queue

from intcodecomputer import Computer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# get program instructions
instructions = parseMod.readCSVInts('data/23networks.csv')

# create fifty computers and give them their own addresses
computers = []
input_queues = [queue.SimpleQueue() for i in range(50)]
for i in range(50):  # create fifty computers and label them
    computers.append(Computer(copy.deepcopy(instructions)))
    input_queues[i].put(i)  # put computer number in the computer
    computers[i].processInput(input_queues[i])  # put appropriate input queue on each

# outputs from computers, content, requested vals
outputs = [[] for i in range(50)]
nat_content = [0, 0]  # x, y
first_y, prev_y = 1, 1  # for tracking the requested values

# continue until computers give the info we want
while True:
    # get the output, populate the input queues, check for a NAT update
    for i in range(len(computers)):
        outputs[i] = computers[i].processInput(input_queues[i])

        for j in range(0, len(outputs[i]), 3):
            if outputs[i][j] == 255:  # signals a NAT
                first_y = outputs[i][j+2] if first_y == 1 else first_y
                nat_content = [outputs[i][j + 1], outputs[i][j + 2]]  # store in the NAT
                continue  # skip queue population

            input_queues[outputs[i][j]].put(outputs[i][j+1])
            input_queues[outputs[i][j]].put(outputs[i][j+2])

    # put -1 values in the empty queue, count how many empty values were used
    count = 0
    for i in range(len(computers)):
        if input_queues[i].empty():
            input_queues[i].put(-1)
            input_queues[i].put(-1)
            count += 1

    # if all queues were empty, idle system, load from NAT
    if count == len(computers):
        if nat_content[1] == prev_y:  # if found the repeat y, end the loop
            break  # done only when the queues are empty and the reset has been found

        # put NAT stuff on the 0 computer queue, drop the -1
        input_queues[0].get()
        input_queues[0].get()
        input_queues[0].put(nat_content[0])
        input_queues[0].put(nat_content[1])

        prev_y = nat_content[1]

# display results
print(f"Part 1 - first y to NAT: {first_y}")
print(f"Part 2 - first duplicate y from NAT: {prev_y}")
