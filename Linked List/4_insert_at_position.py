'''
Positon at 0 = Insert at begining 
in Between = need to traverse
Positon at end = Similar t append (untill the last node is reached)

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtposition(self,position,data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("invalid position/ position inbound")
            return
        
        new_node.next = current.next
        current.next = new_node

    def append(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end =" -> ")
            current = current.next
        print("None")


ll = LinkedList()

ll.append(3)
ll.append(4)

ll.insertAtposition(0,1)
ll.insertAtposition(1,2)

ll.traverse()