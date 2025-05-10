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

    def insert_at_position(self, data, position):
        new_node = Node(data)


    def traverse(self):

        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("none") 


ll = LinkedList()

ll.append(3)
ll.append(1)

ll.insert_at_position(2,1)

ll.traverse()
