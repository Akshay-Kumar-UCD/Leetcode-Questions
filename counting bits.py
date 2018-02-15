"""
class Solution(object):
    def countBits(self, num):
        
        :type num: int
        :rtype: List[int]
        
        list_bits = []
        for i in range(num+1):
            bit = bin(i)
            list_bits.append(bit.count('1'))
        return list_bits
"""