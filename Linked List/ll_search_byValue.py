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
        current = self.head                                             # Stat with the head/ first node of the linkedlist
        while current:                                                  # if a node exists
            if current.data == data:                                    # If the current Node's data mathes the data 
                print(f"Yes found the value - {current.data}")          # Print out the data
                return True                                             # For exiting the loop safely
            current = current.next                                      # Also traverse the linkledlist by setting current.next in evey loop
        print("Value not Found")
        return False                                                    # For exiting the loop safely



ll = LinkedList()

ll.append(23)
ll.append(3434)

ll.search(23)
