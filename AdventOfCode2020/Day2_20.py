# Advent of Code Day 2
# Check password validity of min and max num of certain characters p1
# Check XOR of occurrence of character at specified index; 1 indexing for the non programmers making bad passwords
# Author:   Rachael Judy
# Date:     12/2/2020


import parseMod


# get array of each line, split at spaces
pwd_list = parseMod.readCSV_rowEl('2pswd.csv', ' ')
numValid = 0
for pswd in pwd_list:
    bounds = pswd[0].split('-')
    mini = int(bounds[0])   # min count or index
    maxi = int(bounds[1])   # max count or index
    c = pswd[1][0]      # character looking for

    count = 0
    # For Part 2 - checking character position
    # XOR of occurrence at two spots
    if pswd[2][mini - 1] == c and pswd[2][maxi - 1] != c or\
            pswd[2][mini - 1] != c and pswd[2][maxi - 1] == c:
        numValid += 1

""" 
    # For Part 1 - checking the char count
    for letter in password[2]:
        if letter == c:
            count += 1


    if mini <= count <= maxi:
        numValid += 1
"""

print("Found: ", numValid)