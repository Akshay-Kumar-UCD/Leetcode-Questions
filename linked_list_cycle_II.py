# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        faster = slower = head
        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                break
        else:
            return None
        while slower != head:
            slower,head = slower.next,head.next
        return head