from node import Node

class LinkedList():
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, element):
        if self.head == None:
            self.head = Node(element)
        else:
            current = self.head
            while current.next:
                current = current.next
            newNode = Node(element)
            newNode.prev = current
            current.next = newNode
        self._size += 1

    def remove(self, element):
        if self.head == None:
            raise ValueError("{element} is not in the list.")
        elif self.head.data == element:
            self.head = self.head.next
            return True
        else:
            ancestor = self.head
            current = self.head.next
            while(current):
                if current.data == element:
                    ancestor.next = current.next
                    next = current.next
                    next.prev = current.prev

                    current.next = None
                    current.prev = None
                    self._size -= 1
                    return True
                ancestor = current
                current = current.next

        raise ValueError(f"{element} is not in the list.")

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        current = self.head
        while(current):
            try:
                print(current.data, current.prev.data)
            except:
                pass
            r = r + str(current.data) + " <-> "
            current = current.next
        return r[0:-4]

    def __str__(self):
        return self.__repr__()


myList = LinkedList()

for x in range(0, 10):
    myList.push(x)

print(myList)
print(len(myList))

myList.remove(7)

print(myList)
print(len(myList))