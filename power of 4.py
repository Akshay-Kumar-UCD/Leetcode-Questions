class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num.bit_length()%2==1 and num & (num-1) == 0