class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        final = 0
        i = 0
        while True:
            if i == 10:
                break
            for char in str(n):
                final += (int(char)*int(char))
            n = final
            final = 0
            if n == 1:
                return True
            i += 1
        return False