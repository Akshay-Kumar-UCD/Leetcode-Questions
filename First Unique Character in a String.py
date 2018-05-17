class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        filtered_s = s
        while filtered_s:
            if filtered_s[0] in filtered_s[1:]:
                filtered_s = filtered_s.replace(filtered_s[0],"")
            else:
                return s.find(filtered_s[0])
        return -1