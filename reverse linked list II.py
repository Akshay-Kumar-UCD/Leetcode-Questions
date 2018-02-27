# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        copy = dummy
        tempM, tempN = m,n-m+1
        while tempM > 1:
            copy = copy.next  
            tempM -= 1
        reverse = None
        cur = copy.next
        while tempN > 0:
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
            tempN -= 1
        copy.next.next = cur
        copy.next = reverse
        return dummy.next