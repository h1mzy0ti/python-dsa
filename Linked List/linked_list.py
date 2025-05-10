'''
Basic Implementation of Linked List in Python

Creating and Traversing a List

'''

# Step 1: Defining the structure of the Node

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

# Step 2: Defining the linkedList

class LinkedList:
    def __init__(self):
        self.head = None                            # Starting the linkedlist initially empty

    # Step 3: Insert a new node at the End
    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node                    # If LinledList is empty new ndoe becomes the head
            return
        
        current = self.head
        while current.next:                         # Traverse to the last node
            current = current.next
        current.next = new_node
         
    # Step 4: Traverse and print all nodes
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("none")

# Create the linkedlist by assigning object

ll = LinkedList()

# Append

ll.append(12)
ll.append(23)
ll.append(34)
ll.append(343)

# Traverse
ll.traverse()