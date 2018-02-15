"""

class Solution(object):
    def maximumGap(self, nums):

        :type nums: List[int]
        :rtype: int

        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        max_count = 0
        for i in range(len(nums)-1):
            temp_count = nums[i+1] - nums[i]
            if temp_count > max_count:
                max_count = temp_count
        return max_count
            

"""