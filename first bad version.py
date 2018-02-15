"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
    
        :type n: int
        :rtype: int
    
        a = n
        b = 1
        while b < a:
            c = (a+b) / 2
            if isBadVersion(c):
                a = c
            else:
                b = c + 1
        return b
"""