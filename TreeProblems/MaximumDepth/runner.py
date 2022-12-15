class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def depth_logic(node: Node):
    pass

# def max_depth(root: Node):
#     if not root:
#         return 0

#     left_depth = max_depth(root.left)
#     right_depth = max_depth(root.right)
#     print(left_depth)

def max_depth(root: Node):
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    seven = Node(7)
    six = Node(6)
    five = Node(5)
    four = Node(4)
    three = Node(3,six, seven)
    two = Node(2, four, five)
    root = Node(1,two, three)

    depth = max_depth(root)
    print(depth)



         #          1
         #     2          3
         # 4      5    6      7