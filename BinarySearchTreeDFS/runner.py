from turtle import left


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_first_search_bst_iterative(root: Node):
    if root == None: return []

    ordered_list = []
    stack = [root]
    while(len(stack)>0):
        current = stack.pop()
        ordered_list.append(current.val)
        if(current.right): stack.append(current.right)
        if(current.left): stack.append(current.left)
    return ordered_list

def depth_first_search_bst_recursive(root: Node):
    ordered_list = []
    stack = [root]

    if len(stack)>0:
        current = stack.pop()
        print(current.val)
        
        if current.left:
            depth_first_search_bst_recursive(current.left)
        if current.right:
            depth_first_search_bst_recursive(current.right)
    else:
        return 



    # while(len(stack)>0):
    #     current = stack.pop()
    #     ordered_list.append(current.val)
    #     if(current.right): stack.append(current.right)
    #     if(current.left): stack.append(current.left)
    # return ordered_list


if __name__ =="__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    # ordered_list = depth_first_search_bst_iterative(a)
    ordered_list = depth_first_search_bst_recursive(a)

    print(ordered_list)


#start at root
#check if root is null. Yes? return empty list
# init stack at root

# while there are items in the stack
    #add value of current node
    #push right node to stack
    #push left node into stack
#return list 