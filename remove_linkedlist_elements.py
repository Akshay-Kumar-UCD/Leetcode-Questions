# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        dummy = temp
        while dummy:
            if dummy.next and dummy.next.next and dummy.next.val == val:
                dummy.next = dummy.next.next
            elif dummy.next and dummy.next.val == val:
                dummy.next = None
            else:
                dummy = dummy.next
        return temp.next