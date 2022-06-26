class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


def count(node):
        count = 1
        current = node
        while current.next != None:
            current = current.next
            count += 1
        return count


head = Node(4)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(10)
nodeE = Node(56)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
   
print(count(head))