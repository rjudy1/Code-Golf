# Author:   Rachael Judy
# Date:     12/1/2020
# Purpose:  computer opcodes 1 add, 2 multiply, 99 end

#import os, sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


def processInput(array):
    index = 0
    while index < len(array):
        if array[index] == 1:
            array[array[index + 3]] = array[array[index+1]] + array[array[index+2]]
            index+=3
        elif array[index] == 2:
            array[array[index + 3]] = array[array[index+1]] * array[array[index+2]]
            index += 3
        elif array[index] == 99:
            break
        index += 1
    return array

content = parseMod.readCSV('data/2num.csv', ',')
solution = 0
for i in range(100):
    for j in range(100):
        content = parseMod.readCSV('data/2num.csv', ',')
        content[1] = i
        content[2] = j
        a=processInput(content)
        if a[0] == 19690720:
            print(i)
            print(j)
            solution = i * 100 + j
            break
print("array", a)
print("sol ", solution)