"""
import itertools
class Solution:
    def permuteUnique(self, nums):
        #:type nums: List[int]
        #:rtype: List[List[int]]
        return list(set(list(itertools.permutations(nums))))
"""