# implements nodes
class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

# finds height of tree
def height(root):
    if root is None:
        return 0
    l_height = height(root.left)
    r_height = height(root.right)
    if l_height >= r_height:
        return l_height+1
    else:
        return r_height+1

# prints level of tree
def printGivenLevel(root,level,nodes):
    if root is None:
        return
    if level == 1:
        nodes.append(root)
    else:
        printGivenLevel(root.left,level-1,nodes)
        printGivenLevel(root.right,level-1,nodes)
    return nodes

# prints level order of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        curr_level_nodes = printGivenLevel(root,i,[])
        print(curr_level_nodes[0].data)

# creates tree
root = Node(1)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(7)
root.left.left.right = Node(4)
root.right.right.left = Node(8)
root.right.right.left.left = Node(9)

printLevelOrder(root)