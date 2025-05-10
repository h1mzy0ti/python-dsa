class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def traverse(self):

        current = self.head
        while current:
            print(current.data,end="  ->  ")
            current = current.next
        print("None")

    def delete(self):
        current = self.head
        while current.next:
            current = current.next
        current.next = None


ll= LinkedList()

ll.append(213)

ll.append(4)

ll.append("e")

ll.append(21344)

ll.traverse()
ll.delete()
ll.traverse()