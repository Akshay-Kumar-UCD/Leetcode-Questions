"""
class Solution(object):
    def reverse(self, x):
        
        :type x: int
        :rtype: int
        
        str_x = str(x)
        str_x_rever = str_x[::-1]
        if str_x_rever[-1] is "-":
            temp = str_x_rever
            str_x_rever = list(str_x_rever)
            str_x_rever[0] = "-"
            for i in range(1,len(str_x_rever)):
                str_x_rever[i] = temp[i-1]
        new_str = ""
        for val in str_x_rever:
            new_str += val
        answer = int(new_str)
        overflow = (2**31) - 1
        if (abs(answer) > overflow):
            return 0
        return answer
"""