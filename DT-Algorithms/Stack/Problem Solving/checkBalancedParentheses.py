from stack import Stack

def checkBalancedParentheses(expression):
    opens = ["(", "[", "{"]
    closes = [")", "]", "}"]
    myStack = Stack()
    for symbol in expression:
        if symbol in "({[":
            myStack.push(symbol)
        elif symbol in ")}]":
            if myStack.isEmpty():
                return False
            index = opens.index(myStack.peek())
            if symbol == closes[index]:
                myStack.pop()
    return myStack.isEmpty()

expression = str(input("Write an expression with parentheses for validation: "))
print(checkBalancedParentheses(expression))
