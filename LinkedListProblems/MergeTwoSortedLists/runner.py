class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"Node(val = {self.val}, next={self.next})"


def mergeTwoLists(list1: Node, list2: Node) -> Node:
        cur = dummy = Node()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

if __name__ == "__main__":
    seven = Node(7)
    five = Node(5,seven)
    two = Node(2,five)
    list1 = Node(1,two)

    six = Node(6)
    three = Node(3,six)
    two2 = Node(2,three)
    list2 = Node(1,two2)
    
    new_linked_list = mergeTwoLists(list1, list2)
    print(new_linked_list)


