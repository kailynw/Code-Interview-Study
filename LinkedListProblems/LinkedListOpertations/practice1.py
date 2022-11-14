from re import search


class Node():
    def __init__(self, value):
        self.value= value
        self.next = None

class LinkedList():
    def __init__(self, value):
        self.head= Node(value)

    def add(self, value):
        new_node = Node(value)
        current = self.head
        while current.next!=None:
            current= current.next
        current.next = new_node
    
    def search(self, search_value):
        current= self.head
        while current!=None:
            if(current.value == search_value):
                return current
            current= current.next
        return None

    def delete(self, value):
        searched_node = self.search(value)
        print(searched_node.value)
        if(searched_node!=None):
            searched_node.value = searched_node.next.value
            searched_node.next = searched_node.next.next
        else:
            print("Node does not exist. Cannot be deleted")

    def display(self):
        current= self.head
        all_nodes= []
        while current!=None:
            all_nodes.append(current.value)
            current= current.next
        print(all_nodes)



if __name__ == "__main__":
    linked_list = LinkedList(3)
    linked_list.add(7)
    linked_list.add(6)
    linked_list.add(8)
    linked_list.display()
    linked_list.delete(8)
    linked_list.display()

