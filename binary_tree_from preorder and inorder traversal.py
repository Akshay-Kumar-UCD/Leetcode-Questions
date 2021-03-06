"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):

        #:type preorder: List[int]
        #:type inorder: List[int]
        #:rtype: TreeNode
        
        if inorder:
            i = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[i])
            node.left = self.buildTree(preorder,inorder[:i])
            node.right = self.buildTree(preorder,inorder[i+1:])
            return node
"""