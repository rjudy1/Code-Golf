# Advent of Code 2019 - Day 4
# Author:  Rachael Judy
# Date:    12/2/2020
# Password Confirmation


# see if password meets established conditions
def meetsConditions(number, stage=0):
    adjMet = False
    if len(number) != 6:
        return False

    number = '!' + number + 'a'
    prev = number[0]

    # check for increasing order and adjacent copies
    for i in range(1, 7):
        # check decreasing
        if number[i] < prev:
            return False

        # stage one needs to have to adjacent copies
        if (not stage) and number[i] == prev:
            adjMet = True

        # stage two must have at least one occurrence of two and only two adjacent equal numbers
        elif stage and number[i] == prev and number[i-2] != prev and number[i+1] != prev:
            adjMet = True

        prev = number[i]

    return adjMet


minimum = 138241
maximum = 674034
countA = 0
countB = 0
# check all numbers in range
for i in range(minimum, maximum):
    if meetsConditions(str(i), False): # stage 1
        countA += 1
    if meetsConditions(str(i), True): # stage 2
        countB += 1

print("Possible Passwords A: ", countA)
print("Possible Passwords B: ", countB)
