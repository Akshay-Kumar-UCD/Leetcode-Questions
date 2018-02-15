import bisect
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        res = []
        for num in nums[::-1]:
            index = bisect.bisect_left(arr, num)
            res.append(index)
            arr.insert(index, num)
        return res[::-1]