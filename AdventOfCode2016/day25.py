# Advent of Code 2016 Day 25
# Author:   Rachael Judy
# Purpose:  d12 assembly + d23 tgl + out

import parseMod

ready = False
day = 25
stage = 'a'
year = 2016

# parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv', ' ')

def clock_signal_found(a, min_repetitions=25):
    pc, reg, out_reps = 0, {'a': a, 'b': 0, 'c': 0, 'd': 0}, 0
    get_val = lambda x: reg[x] if x.isalpha() else int(x)
    inv = {'tgl': 'inc', 'dec': 'inc', 'inc': 'dec', 'jnz': 'cpy', 'cpy': 'jnz', 'out': 'inc'}
    while 0 <= pc < len(data):
        try:
            match data[pc][0]:
                case 'cpy': reg[data[pc][2]] = get_val(data[pc][1])
                case 'inc': reg[data[pc][1]] += 1
                case 'dec': reg[data[pc][1]] -= 1
                case 'jnz': pc += (get_val(data[pc][2])-1) * (get_val(data[pc][1])!=0)
                case 'tgl': data[pc+get_val(data[pc][1])][0] = inv[data[pc+get_val(data[pc][1])][0]]
                case 'out':
                    if out_reps % 2 != get_val(data[pc][1]):
                        return False
                    out_reps += 1
                    if out_reps > min_repetitions:
                        return True
        except IndexError:
            pass
        pc += 1
    return False

result = 0
while not clock_signal_found(result): result += 1

# closed form solution - pattern of 101010... > b*c from initial loop
# b, c = int(data[1][1]), int(data[2][1])
# result = (patt if (patt := int((len(bin(b*c))-2)//2*'10', 2)) >= b*c else 4*patt+2) - b*c

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
