class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        length_str_x = len(str_x)
        first_half_str_x = str_x[:length_str_x/2]
        second_half_str_x = str_x[length_str_x/2:][::-1]
        for char1,char2 in zip(first_half_str_x,second_half_str_x):
            if char1 != char2:
                return False
        return True