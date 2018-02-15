"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        #:type nums: List[int]
        #:rtype: TreeNode
        if nums:
            index = nums.index(max(nums))
            node = TreeNode(max(nums))
            node.left = self.constructMaximumBinaryTree(nums[:index])
            node.right = self.constructMaximumBinaryTree(nums[index+1:])
            return node
"""