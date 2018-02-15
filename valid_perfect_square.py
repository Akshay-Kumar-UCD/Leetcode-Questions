class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return True if int(num ** (1/2)) * int(num ** (1/2)) == num else False