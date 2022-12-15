

class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"Node(val = {self.val}, next={self.next})"

def solution(head:Node, n:int):
    fast, slow = head, head
    #Set fast pointer to figure out removal point
    for _ in range(n): 
        fast = fast.next

    #If removal point is at the beginning then remove the first element using head.next 
    if not fast: return head.next


    while fast.next: 
        fast, slow = fast.next, slow.next

    slow.next = slow.next.next
    return head

if __name__ == "__main__":
    four = Node(4)
    three = Node(3,four)
    two = Node(2,three)
    head = Node(1,two)
    
    new_linked_list = solution(head, 4)
    print(new_linked_list)