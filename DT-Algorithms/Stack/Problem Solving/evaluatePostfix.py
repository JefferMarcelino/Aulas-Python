from stack import Stack
from peform import peform

def evaluatePostfix(exp):
    myStack = Stack()
    for x in exp:
        if x in "1234567890":
            myStack.push(x)
        elif x in "*-+":
            operand2 = int(myStack.pop())
            operand1 = int(myStack.pop())

            res = peform(x, operand1, operand2)
            myStack.push(res)
    return myStack.top.data

print(evaluatePostfix("26*68*-")) # 2*6 - 6*8 = -36