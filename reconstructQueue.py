class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        ordered_line = []
        insertion_order = sorted(people, key = lambda (h,k): (-h,k))
        for person in insertion_order: ordered_line.insert(person[1], person)
        return ordered_line