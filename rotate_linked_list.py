"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        #:type head: ListNode
        #:type k: int
        #:rtype: ListNode
        if head is None:
            return None
        if head.next is None:
            return head
        nodes = []
        p = ListNode(0)
        p.next = head
        q = p
        while q.next is not None:
            q = q.next
            nodes.append(q)
        k %= len(nodes)
        if k == 0:
            return head
        h = nodes[-k]
        nodes[-k-1].next = None
        nodes[-1].next = head
        return h
            
"""