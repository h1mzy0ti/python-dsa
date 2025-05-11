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
        new_node = Node(data)                                           # New node 

        if position == 0:                                               # Check is position is 0 or not if 0 it is insert at beginning 
            new_node.next = self.head                                   # point the newnode.next o the slef.head and self.head = new_node
            self.head = new_node
            return

        current = self.head                                              # Start with the head 
        count = 0                                                        # Count for tracking the postion

        while current is not None and count < position - 1:              # Untill current is not noine and the count is < position - 1(before the position)
            current = current.next                                       # Flow the loop to count by current = current.next
            count += 1

        if current is None:                                              # If search the positon by the position is not found print out invalid
            print("invalid position/ position inbound")
            return
        
        new_node.next = current.next                                      # Untill the condition which is count < position - 1reaches 
        current.next = new_node                                           # Change the current next to new.node

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