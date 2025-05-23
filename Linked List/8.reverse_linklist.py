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

    def reverse(self):                                  # time complextiy O(n),O(1)
        current = self.head
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
       

ll = LinkedList()

ll.append(5)
ll.append(4)
ll.append(3)
ll.append(2)
ll.append(1)



ll.traverse()

ll.reverse()

