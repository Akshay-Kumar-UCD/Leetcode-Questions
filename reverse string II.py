class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            return s[::-1]
        split = []
        i = 0
        while i < len(s):
            if i + k < len(s):
                split.append(s[i:i+k])
                i += k
            else:
                split.append(s[i:len(s)])
                break
        j = 1
        answer = ""
        for val in split:
            if j%2 != 0:
                answer += val[::-1]
            else:
                answer += val
            j += 1
        return answer