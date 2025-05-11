'''
Given the head of a sorted linked list, 
delete all duplicates such that each element 
appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

[1] -> [1] -> [2]

        To

   [1] -> [2]
'''
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

    def removeDup(self):
        current = self.head
        previous = None 
        hashset = set()                                             # hashset to keep track of the element 

        while current:                                              # while current it not None  
            if previous and current.data in hashset:                # if there is previous and current data is in the hashset
                previous.next = current.next                        # set teh previous to the current.next skippign the current
            else:                                                   # or
                hashset.add(current.data)                           # add add the element to the hash set
                previous = current                                  # and previous into current
            current = current.next                                  # interate the loop
            
                                                                        
    def removeDup2(self):                                           #
        current = self.head

        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
    
        


    def traverse(self):
        current = self.head

        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()

ll.append(12)
ll.append(2)
ll.append(2)
ll.append(2)
ll.append(2)
ll.append(2)
ll.append(2)
ll.append(1)
ll.append(1)

ll.traverse()

print("\n After removing the duplicates\n")

ll.removeDup2()

ll.traverse()
