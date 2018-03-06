class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answers = []
        for val in nums1:
            if val in nums2 and val not in answers:
                total_count = min(nums1.count(val),nums2.count(val))
                for _ in range(total_count):
                    answers.append(val)
        return answers