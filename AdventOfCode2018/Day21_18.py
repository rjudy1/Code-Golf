# Advent of Code 2018 - Day 21

# Author:   Rachael Judy
# Date:     12/27/2020
# Purpose:  Reverse engineer the assembly code to display the numbers r0 is being checked against for exit
#           Part 1 is the first number and part 2 is the number when output stalls

# ignore annotations on input

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


class Computer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = [0, 0, 0, 0, 0, 0]
        self.pc = 0
        self.ip = -1

        # opcode to name pairing - dict is number : name - initially empty, but set for next time use
        self.opcode = {0: 'eqir', 7: 'eqri', 11: 'eqrr', 13: 'gtri', 10: 'gtrr', 2: 'gtir', 3: 'setr',
                       9: 'bani', 15: 'banr', 5: 'seti', 4: 'mulr', 14: 'borr', 8: 'bori', 1: 'addi',
                       12: 'addr', 6: 'muli'}
        self.executions = {  # used by process()
            'addr' : lambda line: self.registers[line[1]] + self.registers[line[2]],
            'addi' : lambda line: self.registers[line[1]] + line[2],
            'mulr' : lambda line: self.registers[line[1]] * self.registers[line[2]],
            'muli' : lambda line: self.registers[line[1]] * line[2],
            'banr' : lambda line: self.registers[line[1]] & self.registers[line[2]],
            'bani' : lambda line: self.registers[line[1]] & line[2],
            'borr' : lambda line: self.registers[line[1]] | self.registers[line[2]],
            'bori' : lambda line: self.registers[line[1]] | line[2],
            'setr' : lambda line: self.registers[line[1]],
            'seti' : lambda line: line[1],
            'gtir' : lambda line: int(line[1] > self.registers[line[2]]),
            'gtri' : lambda line: int(self.registers[line[1]] > line[2]),
            'gtrr' : lambda line: int(self.registers[line[1]] > self.registers[line[2]]),
            'eqir' : lambda line: int(line[1] == self.registers[line[2]]),
            'eqri' : lambda line: int(self.registers[line[1]] == line[2]),
            'eqrr' : lambda line: int(self.registers[line[1]] == self.registers[line[2]])
        }

        self.history = set()

    def process(self):
        halt = 0
        while halt == 0:
            if self.pc >= len(self.instructions):
                halt = True  # normal exit
                continue

            line = self.instructions[self.pc]

            if '#ip' in line[0]:  # convert the register to a special reg
                self.ip = line[1]
                self.instructions.remove(line)
                continue

            if self.ip != -1:  # handle pc
                self.registers[self.ip] = self.pc

            # execute normal op
            cmd = self.opcode[line[0]] if str(line[0]).isnumeric() else line[0]
            self.registers[line[3]] = self.executions[cmd](line)
            if self.pc == 28:
                if self.registers[4] in self.history:
                    halt = True
                else:
                   self.history.add(self.registers[4])

                print(self.registers[4])

            # reassign pc
            if self.ip != -1:
                self.pc = self.registers[self.ip]
            self.pc += 1

        return halt


instr = parseMod.readCSV_row('data/21program.csv', '\n')
program = []
for i in instr:
    i = i.split()
    program.append([i[0], int(i[1]), int(i[2]), int(i[3])] if len(i) > 2 else [i[0], int(i[1])])


# brute forcing computer, will eventually print part 2, but takes forever
# computer = Computer(copy.deepcopy(program))
# computer.registers[0] = 10720163
# found = computer.process()  # p1:10720163, p2:5885821

# follow the assembly code reverse engineered
r4 = 0  # register 4 to track
s = set()
print("Read first number for part 1 and last number for part 2")
while True:
    r1 = r4 | 0x10000
    r4 = int(instr[8].split()[1])  # read the two input details
    while True:
        r3 = r1 & 0xFF
        r4 += r3
        r4 &= 0xFFFFFF
        r4 *= int(instr[12].split()[2])  # read the input detail that differs
        r4 &= 0xFFFFFF
        if r1 < 256:
            if r4 not in s:  # compares to r4 and r0 - the check
                print(r4)
            s.add(r4)
            break

        r1 = r1 // 256  # gets out of one infinite loop to find the next check it finds
