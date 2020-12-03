# Advent of Code 2020 Day 1
# Author:   Rachael Judy
# Date:     12/1/20
# Subset sum, 3 numbers problem

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


array = parseMod.readCSV("1num.csv", '\n')
found = False
for i in array:
    for j in array:
        for k in array:
            #k = 0 # uncomment this for stage 1
            if i+j+k == 2020:
                print(i, j, k, sep=',')
                if k:
                    print(i*j*k)
                else:
                    print(i*j)
                found = True
                break
        if found:
            break
    if found:
        break