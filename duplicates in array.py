"""
class Solution(object):
    def findDuplicates(self, nums):
        answer = []
        for val in nums:
            if nums[abs(val)-1] < 0:
                answer.append(abs(val))
            else:
                nums[abs(val)-1] *= -1
        return answer
"""