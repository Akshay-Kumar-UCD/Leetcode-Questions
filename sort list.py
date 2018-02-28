# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast, slow = head.next,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        half = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(half)
        return self.mergeSort(l,r)
    def mergeSort(self,l,r):
        """
        : type l: ListNode
        : type r: ListNode
        : rtype: ListNode
        """
        if not l or not r:
            return l or r
        if l.val > r.val:
            l,r = r,l
        head = prev = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                next_ = prev.next
                prev.next = r
                temp = r.next
                r.next = next_
                r = temp
            prev = prev.next
        prev.next = l or r
        return head