class Solution(object):
    def spiralOrder(self, matrix):
        
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if matrix == []:
            return []
        
        def lefttorightROW(matrix,answer,count):
            for i in range(len(matrix[0])):
                if matrix[count][i] not in answer:
                    answer.append(matrix[count][i])
        
        def toptobottomCOL(matrix,answer,count):
            for i in range(len(matrix)):
                if matrix[i][count] not in answer:
                    answer.append(matrix[i][count])
        
        def righttoleftROW(matrix,answer,count):
            for i in reversed(range(len(matrix[0]))):
                if matrix[count][i] not in answer:
                    answer.append(matrix[count][i])
        
        def bottomtotopCOL(matrix,answer,count):
            for i in reversed(range(len(matrix))):
                if matrix[i][count] not in answer:
                    answer.append(matrix[i][count])
        
        answer = []
        r_ltr_count = 0
        c_ttb_count = len(matrix[0]) - 1
        r_rtl_count = len(matrix) - 1
        c_btt_count = 0
        
        while len(answer) < (len(matrix[0]) * len(matrix)):
            lefttorightROW(matrix,answer,r_ltr_count)
            r_ltr_count += 1
            toptobottomCOL(matrix,answer,c_ttb_count)
            c_ttb_count -= 1
            righttoleftROW(matrix,answer,r_rtl_count)
            r_rtl_count -= 1
            bottomtotopCOL(matrix,answer,c_btt_count)
            c_btt_count += 1
        
        return answer