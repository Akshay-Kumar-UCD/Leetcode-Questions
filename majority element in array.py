"""

class Solution(object):
    def majorityElement(self, nums):
        
        :type nums: List[int]
        :rtype: int
        
        count = len(nums) / 2
        nums = sorted(nums)
        for num in nums:
            if nums.count(num) > count:
                return num
            else:
                while num in nums: nums.remove(num)
        

"""