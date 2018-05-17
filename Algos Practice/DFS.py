""" Implements the Tree """
class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

""" Inorder Traversal """
def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)

""" Postorder Traversal """
def printPostorder(root):
    if root is not None:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

""" Preorder Traversal """
def printPreorder(root):
    if root is not None:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)

# Create the tree to level order traverse
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5) 

print("Inorder: ")
printInorder(root)
print("Postorder: ")
printPostorder(root)
print("Preorder: ")
printPreorder(root)