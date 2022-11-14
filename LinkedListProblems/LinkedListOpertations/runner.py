


class Node:
    def __init__(self, val):
        self.val= val
        self.next = None
    def __repr__(self):
        return f"Node(val ={self.val}, next= {self.next})"


class LinkedList:
    def __init__ (self, data):
        self.head = Node(data)

    def add(self, data):
        #traverse through linked list intil there is a insertion point
        node = Node(data)
        current = self.head
        while current.next!=None: #find next open position
            current= current.next
        current.next= node
    
    def delete(self, data):
        searched_node = self.search(data)
        print(f"Searched Node: {searched_node}")
        if searched_node != None:
           #set searched node to the next nodes value, set searched nodes next to the next-next node
            searched_node.val = searched_node.next.val
            searched_node.next = searched_node.next.next
        else:
            print("No node found in linked list")

    
    def search(self, data):
        current = self.head
        while current!=None:
            if (current.val== data):
                return current
            else:
                current=current.next
        return None
        
    # 3 -> 4  -> 5 - > None
    # node_to_be_inserted = Node(5)
    # Node(4, next=Node)
    # Node(4, next=node_to_be_inserted)
    #
    def count_nodes(self):
        current= self.head
        count = 0
        while(current!=None):
            count+=1
            current = current.next
    
    def print(self):
        current = self.head
        print_list = []
        while current!=None:
            print_list.append(current.val)
            current = current.next
        print(print_list)            

    # 3 -> 4 -> 7 -> 8

if __name__ =="__main__":
    linked_list = LinkedList(3)
    linked_list.add(4)
    linked_list.add(6)
    linked_list.add(8)
    linked_list.delete(4)


    print(linked_list.head)
