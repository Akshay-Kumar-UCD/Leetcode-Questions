"""
class Solution(object):
    def findKthLargest(self, nums, k):
        for val in nums:
            max_ = max(nums)
            location = [i for i, j in enumerate(nums) if j == max_]
            if k is 1:
                return max_
            else:
                nums[location[0]] = None
                k -= 1
"""