"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        
        #:type inorder: List[int]
        #:type postorder: List[int]
        #:rtype: TreeNode
        
        if inorder:
            i = inorder.index(postorder.pop())
            node = TreeNode(inorder[i])
            node.right = self.buildTree(inorder[i+1:],postorder)
            node.left = self.buildTree(inorder[:i],postorder)
            return node
"""