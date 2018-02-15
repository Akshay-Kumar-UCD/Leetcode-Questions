"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
    
        :type nums: List[int]
        :rtype: int
        
        countList = []
        count = 0
        for num in nums:
            if num is 1:
                count += 1
            else:
                countList.append(count)
                count = 0
        countList.append(count)
        if len(countList) > 0:
            return max(countList)
        else:
            return 0
        
"""