from stack import Stack


def hasHigherPrec(operator1, operator2):
    operators = ["+", "-", "*"]

    if operator1 == "+" and operator2 == "-":
        return True
    elif operator1 == "-" and operator2 == "+":
        return True

    return operators.index(operator1) > operators.index(operator2)


def infixToPostfix(exp):
    myStack = Stack()
    res = ""

    for x in exp:
        if x in "1234567890":
            res = res + x
        elif x in "+*-":
            while((not myStack.isEmpty()) and hasHigherPrec(myStack.peek(), x)):
                res = res + myStack.peek()
                myStack.pop()
            myStack.push(x)
    
    while(not myStack.isEmpty()):
        res = res + myStack.peek()
        myStack.pop()

    return res

print(infixToPostfix("5+6*9-5*1"))