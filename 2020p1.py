# Subset sum, 3 numbers problem

import input

array = input.readCSV("num.csv", '\n')
found = False
for i in array:
    for j in array:
        for k in array:
            if i+j+k == 2020:
                print(i, j, k, sep=',')
                print(i*j*k)
                found = True
                break
        if found:
            break
    if found:
        break