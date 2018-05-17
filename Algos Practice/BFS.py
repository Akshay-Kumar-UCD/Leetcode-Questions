""" Implements the Tree """
class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

""" Finds height of Tree """
def height(root):
    if root is None:
        return 0
    else:
        lHeight = height(root.left)
        rHeight = height(root.right)
        if lHeight >= rHeight:
            return lHeight+1
        else:
            return rHeight+1

""" Prints Given Level of Tree """
def printGivenLevel(root,level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    else:
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right,level-1)

""" Prints Level Order Traversal of Tree """
def printLevelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        printGivenLevel(root,i)

# Create the tree to level order traverse
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)