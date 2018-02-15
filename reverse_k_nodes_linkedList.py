"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        
        #:type head: ListNode
        #:type k: int
        #:rtype: ListNode
        
        counter, node = 0, head
        while node:
            counter += 1
            node = node.next
        if k <= 1 or counter < k:
            return head
        node, curr = None, head
        for _ in range(k):
            next_ = curr.next
            curr.next = node
            node = curr
            curr = next_
        head.next = self.reverseKGroup(curr,k)
        return node
        
"""