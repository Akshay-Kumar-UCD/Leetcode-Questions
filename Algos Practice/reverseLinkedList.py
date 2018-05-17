""" Implements Nodes of Linked List """
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

""" Creates Linked List """
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node

""" Function to Reverse Linked List """
def reverseList(node):
    prev = None
    curr = node
    while curr is not None:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
    return prev

# Create linked list to reverse
root = LinkedList()
root.push(5)
root.push(4)
root.push(3)
root.push(2)
root.push(1)

temp = root.head
while temp:
    print(temp.data)
    temp = temp.next
print("List Reversed!")
new_list = reverseList(root.head)
while new_list:
    print(new_list.data)
    new_list = new_list.next