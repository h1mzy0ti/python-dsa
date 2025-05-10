'''
Objective - implement a LL to search by value

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

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self,data):                                              # Fucntion containing the data/ value to search
        current = self.head
        while current:
            if current.data == data:
                print(f"Yes found the value - {current.data}")
                current = current.next



ll = LinkedList()

ll.append(23)
ll.append(3434)

ll.search(23)
