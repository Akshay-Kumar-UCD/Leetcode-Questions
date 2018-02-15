"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        #:type lists: List[ListNode]
        #:rtype: ListNode
        answer = []
        for val in lists:
            while val:
                answer.append(val.val)
                val = val.next
        return sorted(answer)

"""