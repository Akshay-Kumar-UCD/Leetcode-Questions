# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        level = [root]
        while any(level):
            answer.append(max(node.val for node in level))
            level = [newLevel for node in level for newLevel in (node.left,node.right) if newLevel]
        return answer