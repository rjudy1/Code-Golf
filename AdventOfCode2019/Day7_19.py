# Advent of Code 2019 Day 7
# Author:   Rachael Judy
# Date Mod: 12/3/2020
# Chained computers

# store permutations somehow - pull out of queue, list of 120?
# find how to route output/next value to next input - keep queues and pop off those instead of input
#       - modify the instruction set?
# loop A-E with same program
# stick output on next input queue?
# feed output into next
# check if exceeded max output so far
# store highest signal output based on permutations

### CURRENTLY HAS DAY 5 CODE
import parseMod


def setParams(array, index):
    x = array[index + 1]
    y = array[index + 2]
    if array[index] % 1000 < 100:
        x = array[x]
    if array[index] % 10000 < 1000:
        y = array[y]
    return x, y


def processInput(array):
    index = 0

    while index != len(array) - 1:
        if array[index] % 100 == 1:  # add next two params to third
            x, y = setParams(array, index)
            array[array[index + 3]] = x + y
            index += 3

        elif array[index] % 100 == 2: # multiply next two params to third
            x, y = setParams(array, index)
            array[array[index + 3]] = x * y
            index += 3

        elif array[index] % 100 == 3:  # take input to next param
            array[array[index+1]] = int(input('Enter num: '))
            index += 1

        elif array[index] % 100 == 4:  # print next param
            x, y = setParams(array, index)
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
            break
        index += 1  # separate in case of garbage numbers
    return array # modify returns?


content = parseMod.readCSV('7num.csv', ',')


# loop through here
processInput(content)
