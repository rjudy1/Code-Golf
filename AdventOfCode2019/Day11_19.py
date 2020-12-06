# Advent of Code 2019 - Day 11

# Author:   Rachael Judy
# Date:     12/4/2020
# Purpose:  Painting robot inputs current color panel and outputs the color and direction to turn
# Created intcode_computer module for future use, eases storage


import queue

import parseMod

# set this for part 0 or 1 (first or second part of problem)
stage = 1


# returns address of value that should be used
def setParams(array, index, base=0):
    # absolute
    x = index + 1
    y = index + 2
    z = index + 3

    if array[index] % 1000 < 100:  # position addressing
        x = array[x]
    elif array[index] % 1000 >= 200:  # relative addressing
        x = array[x] + base

    if array[index] % 10000 < 1000:
        y = array[y]
    elif array[index] % 10000 >= 2000:
        y = array[y] + base

    if array[index] % 100000 < 10000:
        z = array[z]
    elif array[index] % 100000 >= 20000:
        z = array[z] + base

    return x, y, z


# inputQ needs parameter at front and input at back
def processInput(array, inputQ, index=0, feedback=False, base=0):
    output = []
    halt = 0

    while index < len(array):
        x, y, z = setParams(array, index, base)
        if array[index] % 100 == 1:  # add next two params to third
            array[z] = array[x] + array[y]
            index += 3

        elif array[index] % 100 == 2:  # multiply next two params to third
            array[z] = array[x] * array[y]
            index += 3

        elif array[index] % 100 == 3:  # take input to next param
            if not feedback:
                array[x] = inputQ.get() #int(input('Enter num: '))
            else:
                if inputQ.empty():
                    return output, array, index, base  # -10 signifies program is not done
                array[x] = inputQ.get()  # int(input('Enter num: '))
            index += 1

        elif array[index] % 100 == 4:  # print next param
            output.append(array[x])
            print("Output: ", output)
            index += 1

        elif array[index] % 100 == 5:  # jump if true
            if array[x]:
                index = array[y]
                index -= 1
            else:
                index += 2

        elif array[index] % 100 == 6:  # jump if false
            if not array[x]:
                index = array[y]
                index -= 1
            else:
                index += 2

        elif array[index] % 100 == 7:  # less than
            if array[x] < array[y]:
                array[z] = 1
            else:
                array[z] = 0
            index += 3

        elif array[index] % 100 == 8:  # equals
            if array[x] == array[y]:
                array[z] = 1
            else:
                array[z] = 0
            index += 3

        elif array[index] % 100 == 9:  # base + parameter
            base += array[x]
            index += 1

        elif array[index] % 100 == 99:  # end program
            halt = -1
            break

        index += 1  # separate in case of garbage numbers
    if not feedback:
        return output
    else:
        return output, array, halt, base


# display the array as grid
def paintShip(display):
    for row in display:
        for el in row:
            if el == 1:
                print('}{', end='')
            else:
                print('  ', end='')
        print()


# get instructions
instructions = parseMod.readCSV('data/11robot.csv', ',')
for i in range(1000):
    instructions.append(0)

# prep for run
inputQ = queue.SimpleQueue()
inputQ.put(stage)  # prep input with either 0 or 1
ind, stop, direction, base = 0, 0, 100, 0  # direction mod 4 will indicate up, right, down, left

# track panels and number changed
countOfPaints = 0
squaresPainted = []  # will hold tuples of spots visited
panels = [[0 for j in range(75)] for i in range(75)]  # side of ship
x, y = 30, 20  # start in center

# run program until end
while stop != -1:
    out, instructions, ind, base = processInput(instructions, inputQ, ind, True, base)

    # color the panel the output
    panels[y][x] = out[0]

    # check if new square visited - for stage 0 (first part)
    if (x, y) not in squaresPainted:
        countOfPaints += 1
        squaresPainted.append((x, y))

    # turn and move the robot
    turn = out[1]
    direction += (-1 + turn * 2)

    if direction % 4 == 0:
        y -= 1  # up
    elif direction % 4 == 1:
        x += 1  # right
    elif direction % 4 == 2:
        y += 1  # down
    elif direction % 4 == 3:
        x -= 1  # left

    # put sitting panel color in input queue
    inputQ.put(panels[y][x])

    # check if done
    stop = ind

# display results
print("Number of Panels Painted/Visited: ", countOfPaints)
print("Paint job: ")
paintShip(panels)
