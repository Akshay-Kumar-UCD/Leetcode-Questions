"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        #:type l1: ListNode
        #:type l2: ListNode
        #rtype: ListNode
        untraversed = l3 = ListNode(0)
        extra_digit = False
        while l1 or l2:
            if l1 and l2:
                if extra_digit:
                    l1.val += 1
                    extra_digit = False
                temp = str(l1.val + l2.val)
                l3.val = int(temp[-1])
                if l1.val + l2.val > 9:
                    extra_digit = True
                if l1.next is not None or l2.next is not None:
                    l3.next = ListNode(l3.val)
                    l3 = l3.next
                    l1 = l1.next
                    l2 = l2.next
                else:
                    if extra_digit:
                        l3.next = ListNode(1)
                    if l1.next is None and l2.next is None:
                        break
            elif l1:
                if extra_digit:
                    l1.val += 1
                    extra_digit = False
                temp = str(l1.val)
                l3.val = int(temp[-1])
                if l1.val > 9:
                    extra_digit = True
                if l1.next is not None:
                    l3.next = ListNode(l3.val)
                    l3 = l3.next
                    l1 = l1.next
                else:
                    if extra_digit:
                        l3.next = ListNode(1)
                    if l1.next is None:
                        break
            elif l2:
                if extra_digit:
                    l2.val += 1
                    extra_digit = False
                temp = str(l2.val)
                l3.val = int(temp[-1])
                if l2.val > 9:
                    extra_digit = True
                if l2.next is not None:
                    l3.next = ListNode(l3.val)
                    l3 = l3.next
                    l2 = l2.next
                else:
                    if extra_digit:
                        l3.next = ListNode(1)
                    if l2.next is None:
                        break
        return untraversed
"""