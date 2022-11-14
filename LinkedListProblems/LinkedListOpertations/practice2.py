
from email import header


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return (f"val: {self.val} | next: {self.next}")

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, val):
        #check if head node has data, if not add it
        if self.head == None: self.head = Node(val); return

        current = self.head
        #if head has data in it, then find next insertion point and insert the data
        while (current.next != None):
            print(current)
            current = current.next

        current.next = Node(val)

    def delete(self, val):
        if self.head.val == val: self.head = self.head.next

        current = self.head
        
        #find value of node or until there or no more nodes to look for

        while(current.val !=None):
            if(current.val == val):
                current

        #1 ->2 ->3 ->4

    def print_nodes(self):
        current = self.head
        all_nodes = []
        
        while(current!=None):
            all_nodes.append(current.val)
            current = current.next
        
        print(all_nodes)

        


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.delete(90)

    linked_list.print_nodes()