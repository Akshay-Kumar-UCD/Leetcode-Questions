class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return s
        ls = []
        for char in s:
            ls.append(char)
        vowel_string = "aeiouAEIOU"
        i = 0
        j = len(ls)-1
        while i <= j:
            if ls[i] in vowel_string and ls[j] in vowel_string:
                dummy = ls[i]
                ls[i] = ls[j]
                ls[j] = dummy
                i += 1
                j -= 1
            elif ls[i] in vowel_string:
                j -= 1
            elif ls[j] in vowel_string:
                i += 1
            else:
                j -= 1
        ans = ""
        for val in ls:
            ans += val
        return ans