from stack import Stack
from peform import peform


def evaluatePrefix(exp):
    myStack = Stack()
    for x in range(1, len(exp)+1):
        if exp[-x] in "1234567890":
            myStack.push(exp[-x])
        elif exp[-x] in "*-+":
            operand1 = int(myStack.pop())
            operand2 = int(myStack.pop())

            res = peform(exp[-x], operand1, operand2)
            myStack.push(res)
    return myStack.top.data

print(evaluatePrefix("-+*23*549")) # 5*4 + 2*3 - 9 = 17
