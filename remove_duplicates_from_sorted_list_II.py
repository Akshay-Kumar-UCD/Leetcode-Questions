# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        copy = ListNode(0)
        copy.next = head
        curr = copy
        while curr:
            extra_duplicate = False
            while curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                extra_duplicate = True
                curr.next = curr.next.next
            if extra_duplicate:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return copy.next
            