class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answers = []
        for val in nums1:
            if val in nums2 and val not in answers:
                answers.append(val)
        return answers