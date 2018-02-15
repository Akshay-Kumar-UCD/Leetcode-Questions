"""
class Solution(object):
    def singleNumber(self, nums):
        
        :type nums: List[int]
        :rtype: int
        
        nums = sorted(nums)
        if len(nums) is 1:
            return nums[0]
        else:
            for i in range(1,len(nums)):
                if i % 2 is not 0 and nums[i] != nums[i-1]:
                    return nums[i-1]
        return nums[-1]
"""