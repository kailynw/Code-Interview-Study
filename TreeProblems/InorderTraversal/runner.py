class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

    def __str__(self):
      return f"Node(val= {self.val}, left= {self.left}, right={self.right})"

def traversalHelp(node:TreeNode, traversal_list:list):
    #check if node is empty
    if node == None:
        return
    
    traversalHelp(node.left, traversal_list)
    traversal_list.append(node.val)
    traversalHelp(node.right, traversal_list)
    
def inorderTraversal(root: TreeNode) -> list:
    traversal_list = []
    traversalHelp(root, traversal_list)
    return traversal_list


if __name__ == "__main__":
    six = TreeNode(6)
    five = TreeNode(5)
    four = TreeNode(4)
    three = TreeNode(3,five, six)
    two = TreeNode(2, three, four)
    root = TreeNode(1,two, three )

    traversal_list = inorderTraversal(root)
    print(traversal_list)

        