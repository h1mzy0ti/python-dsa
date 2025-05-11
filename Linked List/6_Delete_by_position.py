'''
Deleting a node in a specific posiion

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    # Insert at beginning here 
    def append(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def delete(self,position):
        current = self.head
        previous = None
        count = 0
        
        while current:
            if count == position:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                    return

            previous = current
            current = current.next
            count += 1


    def traverse(self):
        current = self.head

        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()

ll.append(12)
ll.append(2)
ll.append(1)

ll.traverse()

print("\n After deletion\n")

ll.delete(0)

ll.traverse()
