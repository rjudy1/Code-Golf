# Advent of Code 2019 - Day 9

# Author:   Rachael Judy
# Date:     12/3/2020
# Purpose:


import copy
import queue
import itertools

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# set this for part 0 or 1 (first or second part of problem)
part = 1


def setParams(array, index):
    x = array[index + 1]
    y = array[index + 2]
    if array[index] % 1000 < 100:
        x = array[x]
    if array[index] % 10000 < 1000:
        y = array[y]
    return x, y


# inputQ needs parameter at front and input at back
def processInput(array, inputQ, index = 0, feedback = False):
    output = 0
    halt = 0
    while index < len(array):
        if array[index] % 100 == 1:  # add next two params to third
            x, y = setParams(array, index)
            array[array[index + 3]] = x + y
            index += 3

        elif array[index] % 100 == 2: # multiply next two params to third
            x, y = setParams(array, index)
            array[array[index + 3]] = x * y
            index += 3

        elif array[index] % 100 == 3:  # take input to next param
            if not feedback:
                array[array[index+1]] = inputQ.get() #int(input('Enter num: '))
            else:
                if inputQ.empty():
                    return output, array, index  # -10 signifies program is not done
                array[array[index + 1]] = inputQ.get()  # int(input('Enter num: '))
            index += 1

        elif array[index] % 100 == 4:  # print next param
            x, y = setParams(array, index)
            output = x
            print("Output: ", x)
            index += 1

        elif array[index] % 100 == 5:  # jump if true
            x, y = setParams(array, index)
            if x:
                index = y
                index -= 1
            else:
                index += 2

        elif array[index] % 100 == 6:  # jump if false
            x, y = setParams(array, index)
            if not x:
                index = y
                index -= 1
            else:
                index += 2

        elif array[index] % 100 == 7:  # less than
            x, y = setParams(array, index)
            if x < y:
                array[array[index + 3]] = 1
            else:
                array[array[index + 3]] = 0
            index += 3

        elif array[index] % 100 == 8:  # equals
            x, y = setParams(array, index)
            if x == y:
                array[array[index + 3]] = 1
            else:
                array[array[index + 3]] = 0
            index += 3

        elif array[index] % 100 == 99:  # end program
            halt = -1
            break

        index += 1  # separate in case of garbage numbers
    if not feedback:
        return output
    else:
        return output, array, halt


instructions = parseMod.readCSV('7num.csv', ',')


# loop through here
if not part:
    permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
    inputQ = queue.SimpleQueue()
    maxT = 0
    bestSeq = permutations[0]
    # check all possible permutations
    for p in permutations:
        imp = 0  # input to each phase, set be output from previous
        for phase in p:
            inputQ.put(phase)
            inputQ.put(imp)

            # compute next
            imp = processInput(copy.deepcopy(instructions), inputQ)

        maxT = max(maxT, imp)
    print(maxT)

# For second part of problem - uses feedback
else:
    permutations = list(itertools.permutations([5, 6, 7, 8, 9]))
    inputQ = queue.SimpleQueue()
    maxT = 0

    # each amp will have instructions in progress
    for p in permutations:
        instructionSet = [copy.deepcopy(instructions), copy.deepcopy(instructions),
                          copy.deepcopy(instructions), copy.deepcopy(instructions),
                          copy.deepcopy(instructions)]
        insPtr = [0, 0, 0, 0, 0]
        imp = 0

        # initialize all the amps with phase setting and initial loop
        ampNum = 0
        for phase in p:
            inputQ.put(phase)
            inputQ.put(imp)
            # loop, set feedback true
            imp, instructionSet[ampNum], insPtr[ampNum] = processInput(instructionSet[ampNum],
                                                                       inputQ, insPtr[ampNum], True)
            ampNum += 1

        # feedback until the last amp hits end of program
        stop = 0
        while stop != -1:
            for num in range(len(instructionSet)):
                inputQ.put(imp)
                imp, instructionSet[num], insPtr[num] \
                    = processInput(instructionSet[num], inputQ, insPtr[num], True)
                stop = insPtr[num]

        maxT = max(maxT, imp)  # store best thruster setting
    print(maxT)
