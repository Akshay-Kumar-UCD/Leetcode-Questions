class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = ""
        for char in s.split()[::-1]:
            string += char + " "
        return string[:-1]