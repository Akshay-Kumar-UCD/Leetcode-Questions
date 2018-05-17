class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq_dict = {}
        ans = ""
        for char in s:
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
        for key in sorted(freq_dict,key=freq_dict.get)[::-1]:
            while freq_dict[key] > 0:
                ans += key
                freq_dict[key] -= 1
        return ans