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


    def delete(self, data):
        current = self.head
        previous = None
        
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                previous = current
                current = current.next


    def traverse(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("none") 


ll = LinkedList()

ll.append(3)
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(1)

ll.delete(1)

ll.traverse()
