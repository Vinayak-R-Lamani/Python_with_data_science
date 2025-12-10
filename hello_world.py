
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        
        if not self.head:
            self.head =new_node
            return 
            
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    def display(self):

        curr = self.head
        while curr:
            print(f"{curr.val}->" , end= "")
            curr = curr.next
        print('None')

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.display()
        