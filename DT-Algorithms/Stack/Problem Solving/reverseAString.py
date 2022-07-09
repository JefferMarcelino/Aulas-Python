from stack import Stack

myStack = Stack()
text = str(input("Enter a string: "))

for x in text:
    myStack.push(x)

reversedText = ""

for x in range(len(text)):
    reversedText += myStack.peek()
    myStack.pop()

print(reversedText)
