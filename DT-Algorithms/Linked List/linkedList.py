from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, element):
        if self.head: 
            current = self.head 
            while current.next:
                current = current.next
            current.next = Node(element)
        else: 
            self.head = Node(element)
        self._size += 1

    def index(self, element):
        """ Return the index element """
        current = self.head
        i = 0
        while(current):
            if current.data == element:
                return i
            current = current.next
            i += 1
        raise ValueError(f"{element} is not in the list.")

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        current = self.head
        for x in range(index):
            if current:
                current = current.next
            else:
                raise IndexError("list index out of range")
        if current:
            return current.data
        raise IndexError("list index out of range")
        
    def __setitem__(self, index, element):
        current = self.head
        for x in range(index):
            if current:
                current = current.next
            else:
                raise IndexError("list index out of range")
        if current:
            current.data = element
        else:
            raise IndexError("list index out of range")

myList = LinkedList()
myList.push(10)
myList.push(20)
myList.push(30)

print(myList.index(10))