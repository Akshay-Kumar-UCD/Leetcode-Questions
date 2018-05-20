# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        dummy = head
        while head:
            if head.next:
                if head.val == head.next.val:
                    if head.next.next:
                        head.next = head.next.next
                        continue
                    else:
                        head.next = None
            head = head.next
        return dummy