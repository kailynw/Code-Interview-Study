class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

    def __str__(self):
      return f"Node(val= {self.val}, left= {self.left}, right={self.right})"


    
def zigZagTraversal(root: TreeNode) -> list:
    # Base Case
    if root is None:
        return
 
    # Create two stacks to store current
    # and next level
    currentLevel = []
    nextLevel = []
 
    # if ltr is true push nodes from
    # left to right otherwise from
    # right to left
    ltr = True
 
    # append root to currentlevel stack
    currentLevel.append(root)
 
    # Check if stack is empty
    while len(currentLevel) > 0:
        # pop from stack
        temp = currentLevel.pop(-1)
        # print the data
        print(temp.val, " ", end="")
 
        if ltr:
            # if ltr is true push left
            # before right
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            # else push right before left
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)
 
        if len(currentLevel) == 0:
            # reverse ltr to push node in
            # opposite order
            ltr = not ltr
            # swapping of stacks
            currentLevel, nextLevel = nextLevel, currentLevel


if __name__ == "__main__":
    six = TreeNode(6)
    five = TreeNode(5)
    four = TreeNode(4)
    three = TreeNode(3,five, six)
    two = TreeNode(2, three, four)
    root = TreeNode(1,two, three )
    print(root)

    traversal_list = zigZagTraversal(root)

        