class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = set()
        triple = set()
        for n in nums:
            if n not in single:
                single.add(n)
            else:
                triple.add(n)
        return list(single-triple)[0]