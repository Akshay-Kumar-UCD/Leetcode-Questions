"""
class Solution(object):
    def hammingDistance(self, x, y):
        :type x: int
        :type y: int
        :rtype: int
        x_bin, y_bin = bin(x), bin(y)
        x_bin, y_bin = x_bin[2:], y_bin[2:]
        x_bin, y_bin = x_bin[::-1], y_bin[::-1]
        bin_range = bin(max(x,y))
        bin_range = bin_range[2:]
        if len(x_bin) is not len(bin_range):
            x_bin += "0"*(len(bin_range)-len(x_bin))
        if len(y_bin) is not len(bin_range):
            y_bin += "0"*(len(bin_range)-len(y_bin))
        count = 0
        for i in range(len(bin_range)):
            try:
                if x_bin[i] is not y_bin[i]:
                    count += 1
            except IndexError:
                count += 1
        return count
"""