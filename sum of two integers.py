class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        list_ = [a,b]
        return sum(list_)

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        for _ in xrange(32):
            a, b = a^b, (a&b)<<1
        return a if a & 0x80000000 else a & 0xffffffff