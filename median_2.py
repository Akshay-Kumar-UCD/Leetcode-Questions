def merge(a,b):
    c = a + b
    c.sort()
    if len(c) % 2 != 0:
        return c[len(c)/2]
    else:
        x = len(c)/2
        x = int(x)
        return (c[x] + c[x-1])/2

def test():
    n1 = [1,2]
    n2 = [3,4]
    return merge(n1,n2)

if __name__ == "__main__":
    print(test())


"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        
        c = nums1 + nums2
        c.sort()
        if len(c) % 2 != 0:
            return float(c[len(c)/2])
        else:
            x = len(c)/2
            x = int(x)
            return float(c[x] + c[x-1])/2

"""
