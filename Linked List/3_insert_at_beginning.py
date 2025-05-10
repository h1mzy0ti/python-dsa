class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):                                      # Insert ata the ebginning or every new  will be head untill new node ocmes in

        new_node = Node(data)                                   
        new_node.next = self.head                               # First set the new node's next o current head
        self.head = new_node                                    # After doing the above step now the head is set to the new_node
        
    def traverse(self):
        current = self.head

        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("none")


ll = LinkedList()

ll.append(234)
ll.append(23)
ll.append(2)
ll.append(0)

ll.traverse()