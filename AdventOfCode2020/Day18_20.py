# Advent of Code 2020 - Day 18

# Author:   Rachael Judy
# Date:     12/18/2020
# Purpose:  Evaluate sets of equations based on changing the precedence of + and * operators

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


def eval(eq, op_prec):
    op_stack = list()
    num_stack = list()

    for s in eq.split():
        if s in op_prec:  # one of *, +; performs the higher precedence previous stored operation
            while len(op_stack) > 0 and op_prec[s] <= op_prec[op_stack[-1]]:
                op = op_stack.pop()
                num1 = num_stack.pop()
                num2 = num_stack.pop()

                res = operations[op](num1, num2)
                num_stack.append(res)

            op_stack.append(s)  # put operation s on the op_stack

        elif s[0] == '(':  # evaluator will run until it hits the closing one of this
            while s[0] == '(':  # catch the nested (
                op_stack.append('(')  # acts as a blocking to know how far can be evaluated
                s = s[1:]
            num_stack.append(int(s))  # add the internal number to num_stack

        elif s[-1] == ')':  # if found a closing parenthesis
            num_stack.append(int(s[:s.index(')')]))  # append the number before the chain of these
            while s[-1] == ')':  # back up the chain
                s = s[:-1]

                while True:  # perform the operations in the set of parenthesis until we hit a new (
                    # compute result
                    op = op_stack.pop()
                    if op == '(':
                        break

                    num1 = num_stack.pop()
                    num2 = num_stack.pop()

                    result = operations[op](num1, num2)
                    num_stack.append(result)  # put it back in the operand pile for next use

        else:  # if not one of the operators, throw the number on the num_stack for use with the op
            num_stack.append(int(s))

    # execute the final set L->R without parenthesis to guide the precedence
    while len(op_stack) > 0:
        op = op_stack.pop()
        num1 = num_stack.pop()
        num2 = num_stack.pop()

        result = operations[op](num1, num2)
        num_stack.append(result)

    return num_stack.pop()  # the final result


lines = parseMod.readCSV_row('data/18math.csv', '\n')

# existing operations
operations = {
    '+': lambda num1, num2: num1 + num2,
    '*': lambda num1, num2: num1 * num2
}

# part 1
operator_precedence = {
    '+': 1,
    '*': 1,
    '(': 0
}
evals = []  # store the evaluation of each line
for equation in lines:
    evals.append(eval(equation, operator_precedence))

print("Part 1: ", sum(evals))

# part 2
evals =[]
operator_precedence['+'] = 2  # addition is higher precedence than multiplication now, change precedence
for equation in lines:
    evals.append(eval(equation, operator_precedence))

print("Part 2: ", sum(evals))
