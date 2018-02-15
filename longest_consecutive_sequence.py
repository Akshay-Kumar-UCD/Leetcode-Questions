class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans,s = 0,set()
        for num in nums:
            s.add(num)
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                j = nums[i]
                while j in s:
                    j += 1
                ans = max(ans,j-nums[i])
        return ans