# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        # find middle node
        slower,faster = head, head.next.next
        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
        # got root 
        copy = slower.next
        slower.next = None
        root = TreeNode(copy.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(copy.next)
        
        return root