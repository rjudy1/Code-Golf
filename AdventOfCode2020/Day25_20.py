# Advent of Code 2020 - Day 25
# Author:   Rachael Judy
# Date:     12/25/2020
# Purpose:  Find loop size to generate public key and use loop size with other public key to find private key (RSAish)

inp = [8252394, 6269621]  # encryption keys go here (your input)
loop_size, value = 0, 0  # checks against value, using incrementing loop size
while value != inp[0] and value != inp[1]:
    loop_size += 1
    value = pow(7, loop_size, 20201227)  # subject key, loop size, modulus (change consts if your stmt differs)

print("private encryption key: ", pow(inp[value==inp[0]], loop_size, 20201227))  # other key, loop_size, mod num
