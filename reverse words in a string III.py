class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""
        for char in s.split():
            answer += char[::-1] + " "
        return answer[:-1]