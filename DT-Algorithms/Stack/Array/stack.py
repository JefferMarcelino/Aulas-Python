class Stack:
    def __init__(self):
        self.top = -1
        self._size = 0
        self._stack = [None]*10

    def push(self, element):
        self._stack[self.top + 1] = element
        self.top += 1

    def pop(self):
        self.top -= 1

    def top(self):
        return self._stack[self.top]

    def __str__(self):
        return self._stack


myStack = Stack()
for x in range(5):
    myStack.push(x)

print(myStack._stack)
print(myStack.top)

myStack.pop()
print(myStack._stack)
print(myStack.top)
