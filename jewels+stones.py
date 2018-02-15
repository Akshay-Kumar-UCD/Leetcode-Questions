"""
class Solution(object):
    def numJewelsInStones(self, J, S):
        
        :type J: str
        :type S: str
        :rtype: int
        
        J_bank = []
        count = 0
        for char in J:
            J_bank.append(char)
        for char in S:
            if char in J_bank:
                count += 1
        return count
"""