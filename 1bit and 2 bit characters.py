"""
class Solution(object):
    def isOneBitCharacter(self, bits):
    
        :type bits: List[int]
        :rtype: bool
    
        bit_str = str(bits[0])
        for i in range(1,len(bits)):
            if bit_str == "0" or len(bit_str) == 2:
                bit_str = ""
                bit_str += str(bits[i])
            elif bit_str == "1":
                bit_str += str(bits[i])
        if len(bit_str) > 1:
            return False
        else:
            return True
        
"""