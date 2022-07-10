from stack import Stack

def checkBalancedParentheses(expression):
    opens = ["(", "[", "{"]
    closes = [")", "]", "}"]
    myStack = Stack()
    print(myStack)
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

print(checkBalancedParentheses("a(a*b)+b(a+2)"))
print(checkBalancedParentheses("a(a*b)+b(a+2))))"))
