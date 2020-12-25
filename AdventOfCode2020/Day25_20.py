# Advent of Code 2020 - Day 25
# Author:   Rachael Judy
# Date:     12/25/2020
# Purpose:  Find loop size and use with other public for privatek (15 sec for 3 lines, adding value var makes it 8 sec)

inp, loop_size, value = [6269621, 8252394], 0, 0  # encryption keys, checks against value, using incrementing loop size
while pow(7, loop_size, 20201227) != inp[0] and pow(7, loop_size, 20201227) != inp[1]:  loop_size += 1
print("private encryption key: ", pow(inp[pow(7, loop_size, 20201227)==inp[0]], loop_size, 20201227))  # other key, loop_size, mod num
