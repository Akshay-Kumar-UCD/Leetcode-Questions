class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        single = set()
        double = set()
        for n in nums:
            if n not in single:
                single.add(n)
            else:
                double.add(n)
        return list(single-double)