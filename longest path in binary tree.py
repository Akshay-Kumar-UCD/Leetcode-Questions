# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_ = 0
        
        def DFS(root):
            if root:
                    left,right = DFS(root.left),DFS(root.right) 
                    self.max_ = max(self.max_,left+right) 
                    return 1+max(left,right)
            else:
                return 0
        
        DFS(root)
        return self.max_