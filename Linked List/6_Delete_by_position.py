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

    def delete(self,position):                              # Typically similar to the search by value but few changes have to be made
        current = self.head 
        previous = None
        count = 0
        
        while current:
            if count == position:                           # if the positon is found 
                if previous:                                # I previous is there   
                    previous.next = current.next            # Set the previous next to the currrent next skipping the current data
                else:                                       # Else or the head is the postion 
                    self.head = current.next                # Connect teh head to the current.next
                    return                                  # Return (sice unlike the delete by value we wanted to delte every element ins thell tha  is simialr to the value)

            previous = current                              # Until we find the positon update previous to current
            current = current.next                          # Until we find the postion update the current to current.next so that it iterates as well
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
