"""
class Solution(object):
    def hasAlternatingBits(self, n):
        
        :type n: int
        :rtype: bool
        
        binary_string = bin(n)
        binary_string = binary_string[2:]
        counter = True
        i = 1
        for bit in binary_string:
            try:
                if (bit == binary_string[i]):
                    counter = False
            except: IndexError
            i += 1
        return counter
        
"""