# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxUtil(root):
            if root is None:
                return 0
            l = maxUtil(root.left)
            r = maxUtil(root.right)
            max_single = max(max(l,r)+root.val, root.val)
            max_top = max(max_single, l+r+root.val)
            maxUtil.res = max(maxUtil.res, max_top)
            return max_single
        
        maxUtil.res = float("-inf")
        maxUtil(root)
        return maxUtil.res