# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        faster = slower = head
        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
        reverse = None
        while slower:
            next_ = slower.next
            slower.next = reverse
            reverse = slower
            slower = next_
        while reverse:
            if reverse.val != head.val:
                return False
            reverse = reverse.next
            head = head.next
        return True
            