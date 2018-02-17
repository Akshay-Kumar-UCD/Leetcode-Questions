class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_min = temp_max = true_max = nums[0]
        for i in range(1, len(nums)):
            temp_min, temp_max = min(nums[i], nums[i] + temp_max, nums[i] + temp_min), max(nums[i], nums[i] + temp_max, nums[i] + temp_min)
            true_max = max(true_max, temp_max)
        return true_max