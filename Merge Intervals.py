# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        end_ = []
        for x in sorted(intervals, key=lambda x: x.start):
            if end_ and x.start <= end_[-1].end:
                end_[-1].end = max(end_[-1].end, x.end)
            else:
                end_ += x,
        return end_