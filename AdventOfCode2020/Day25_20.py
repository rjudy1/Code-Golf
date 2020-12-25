# Advent of Code 2020 - Day 25
# Author:   Rachael Judy
# Date:     12/25/2020
# Purpose:  Do transform (pow) to find loop size; perform transform on other key with other loopsize (15s -add v to 1/2)

# checks using incrementing loop_size - start at known option, transform till match, var inp is your input in array form
loop_size, inp = 0, [6269621, 8252394]  # initial size and input (your puzzle input)
while pow(7, loop_size, 20201227) != inp[0] and pow(7, loop_size, 20201227) != inp[1]:  loop_size += 1  # first match
print("private key: ", pow(inp[pow(7, loop_size, 20201227)==inp[0]], loop_size, 20201227))  # other key, loop_size, mod
