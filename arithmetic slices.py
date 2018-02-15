"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        
        :type A: List[int]
        :rtype: int
        
        dp = 0
        last_slice_length = 1
        for i in range(1, len(A)):
            if last_slice_length >= 2 and A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp = last_slice_length - 1 + dp
                last_slice_length = last_slice_length + 1
            else:
                last_slice_length = 2
        return dp
            
"""