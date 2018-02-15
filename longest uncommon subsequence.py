"""
class Solution(object):
    def findLUSlength(self, a, b):
        
        :type a: str
        :type b: str
        :rtype: int
        
        if (a != b):
            if (len(a) > len(b)):
                return len(a)
            else:
                return len(b)
        elif (a == b):
            return -1
        else:
            while (a):
                a = a[1:]
                if (a != b):
                    if (len(a) > len(b)):
                        return len(a)
                    else:
                        return len(b)
                elif (a == b):
                    return -1
                
        
"""