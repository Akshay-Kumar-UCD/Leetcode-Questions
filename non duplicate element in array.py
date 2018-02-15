"""
from collections import Counter

class Solution(object):
    def singleNonDuplicate(self, nums):
        nums = [k for k, v in Counter(nums).iteritems() if v == 1]
        return nums[0]

"""