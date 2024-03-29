class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next

if __name__ == "__main__":
    three = ListNode(3)
    two = ListNode(2, three)
    one = ListNode(1, two)

    nine = ListNode(9)
    five = ListNode(5, nine)
    four = ListNode(4, five)

    """ 
        1 -> 2 -> 3
        4 -> 5 -> 9

        321 + 954 = 1275

        5 -> 7 -> 2 ->1

    """

    result = addTwoNumbers(one, four)
    print(result.val)
    print(result.next.val)
    print(result.next.next.val)

    


