class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_ = bin(num)[2:]
        answer = ""
        for char in bin_:
            if char == "1":
                answer += "0"
            else:
                answer += "1"
        return int(answer,2)