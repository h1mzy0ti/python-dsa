'''
To Delete if we have full access to the node and linkedList class -
We have to track a previous if previous exists then replace the previous.next to the current.next
if current.data == data(or the value we want) other wise self.head == current.next

and current = current.next

and if not current.data == value
we do -
current = previous
current = current.next
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 


    def traverse(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("none") 

# Objective here is to remove all the elements


ll = LinkedList()

ll.append(3)
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(1)

ll.traverse()
