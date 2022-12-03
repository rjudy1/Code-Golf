# Advent of Code 2019 - Day 9

# Author:   Rachael Judy
# Date:     12/3/2020
# Purpose:  Adds new addressing mode - relative addressing


import queue

import parseMod

# set this for part 1 or 2 (first or second part of problem)
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
def processInput(array, inputQ, index=0, feedback=False):
    output = 0
    halt = 0
    base = 0
    for i in range(1000):
        array.append(0)
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
                    return output, array, index  # -10 signifies program is not done
                array[x] = inputQ.get()  # int(input('Enter num: '))
            index += 1

        elif array[index] % 100 == 4:  # print next param
            output = array[x]
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
        return output, array, halt


instructions = parseMod.readCSVInts('data/9instr.csv', ',')

inputQ = queue.SimpleQueue()
inputQ.put(stage)
processInput(instructions, inputQ)
