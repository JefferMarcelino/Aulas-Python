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

    def insert(self, index, element):
        node = Node(element)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            current = self._getNode(index - 1)
            node.next = current.next
            current.next = node
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
                    current.next = None
                    return True
                    self._size -= 1
                ancestor = current
                current = current.next
        
        raise ValueError(f"{element} is not in the list.")

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def recursionReverse(self, current):
        #current = self.head
        if current.next == None:
            self.head = current
            return True
        self.recursionReverse(current.next)
        next = current.next
        next.next = current
        current.next = None
            
    def _getNode(self, index):
        current = self.head
        for x in range(index):
            if current:
                current = current.next
            else:
                raise IndexError("list index out of range")
        return current

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        current = self._getNode(index)
        if current:
            return current.data
        raise IndexError("list index out of range")
        
    def __setitem__(self, index, element):
        current = self._getNode(index)
        if current:
            current.data = element
        else:
            raise IndexError("list index out of range")

    def __repr__(self):
        r = ""
        current = self.head
        while(current):
            r = r + str(current.data) + " -> "
            current = current.next
        return r[0:-3]

    def __str__(self):
        return self.__repr__()


myList = LinkedList()

for x in range(1, 10):
    myList.push(x)

print(myList)
myList.recursionReverse(myList.head)
print(myList)
