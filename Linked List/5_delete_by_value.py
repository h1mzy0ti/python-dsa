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

    def delete(self,value):
        current = self.head                                     # start with Head
        previous = None                                         # Intialize previous to link that to current.next since we will selete the current

        while current:                                          # while current is available 
            if current.data == value:                           # And if the current.data is  = to the value we are finding
                if previous:                                    # Also if it hase teh previous
                    previous.next = current.next                # wepoint the previous.next = current.next (skipping the current)
                else:                                           # If not previous most probabily it is the start of the list so we define the head to the current.next
                    self.head = current.next
                current = current.next                          # And also keep the search continue
            else:                                               # if we dont find any element we continue the search by default
                previous = current
                current = current.next


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

ll.delete(1)

ll.traverse()
