# Advent of Code 2020 - Day 8

# Author:   Rachael Judy
# Date:     12/8/2020
# Purpose:  Build computer with instructions jmp, acc, nop
#               find loop (1) and correction that removes loop (2)


import sys, os
import copy
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


# GameConsole class for computing
class GameConsole:
    def __init__(self, instr):
        self.pc = 0
        self.acc = 0
        self.visited = []
        self.instructions = instr

    # run the program, if check_terminal, perform check for loop
    def compute(self, check_loop=False):
        while self.pc < len(self.instructions):
            instruction = self.instructions[self.pc]
            if check_loop:
                if self.pc not in self.visited:
                    self.visited.append(self.pc)
                else:
                    return -1  # indicates termination due to infinite loop

            if self.pc >= len(self.instructions):
                return 0
            elif instruction[0] == 'acc':  # add to accumulator
                self.acc += int(instruction[1])
                self.pc += 1
            elif instruction[0] == 'jmp':  # jump argument lines
                self.pc += int(instruction[1])
            elif instruction[0] == 'nop':  # go on, no operation
                self.pc += 1


# read input instructions
instr = parseMod.readCSV_rowEl('data/8instructions.csv', ' ')

# part 1 - find accumulator at infinite loop
print("PART 1")
console = GameConsole(instr)
code = console.compute(check_loop=True)
print("Acc at first loop: ", console.acc)
print()

# find accumulator on correct done, presuming incorrect jmp or nop switch
print("PART 2")
for i in range(len(instr)):
    # copy instructions, fix one error
    copyInstructions = copy.deepcopy(instr)
    if copyInstructions[i][0] == 'jmp':
        copyInstructions[i][0] = 'nop'
    elif copyInstructions[i][0] == 'nop':
        copyInstructions[i][0] = 'jmp'

    # reinitialize computer, run, check for proper termination (code 0)
    console = GameConsole(copyInstructions)
    if not console.compute(check_loop=True):
        print('Correct Termination Acc: ', console.acc)
        print('Incorrect Line', i, instr[i])
        break
