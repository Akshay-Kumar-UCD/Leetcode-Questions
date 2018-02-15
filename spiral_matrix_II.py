def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    
    if n == 0:
        return []
    
    elif n == 1:
        return [[1]]
    
    def lefttorightROW(matrix,answer,count):
        for i in range(len(matrix[0])):
            if matrix[count][i] == 0:
                matrix[count][i] = answer
                answer += 1
        return matrix,answer
    
    def toptobottomCOL(matrix,answer,count):
        for i in range(len(matrix)):
            if matrix[i][count] == 0:
                matrix[i][count] = answer
                answer += 1
        return matrix,answer
    
    def righttoleftROW(matrix,answer,count):
        for i in reversed(range(len(matrix[0]))):
            if matrix[count][i] == 0:
                matrix[count][i] = answer
                answer += 1
        return matrix,answer
    
    def bottomtotopCOL(matrix,answer,count):
        for i in reversed(range(len(matrix))):
            if matrix[i][count] == 0:
                matrix[i][count] = answer
                answer += 1
        return matrix,answer
    
    answer = 1
    width = height = n
    matrix = [[0 for x in range(width)] for y in range(height)]
    r_ltr_count = 0
    c_ttb_count = len(matrix[0]) - 1
    r_rtl_count = len(matrix) - 1
    c_btt_count = 0
    
    while answer < (n * n)+1:
        matrix,answer = lefttorightROW(matrix,answer,r_ltr_count)
        r_ltr_count += 1
        matrix,answer = toptobottomCOL(matrix,answer,c_ttb_count) 
        c_ttb_count -= 1
        matrix,answer = righttoleftROW(matrix,answer,r_rtl_count)
        r_rtl_count -= 1
        matrix,answer = bottomtotopCOL(matrix,answer,c_btt_count)
        c_btt_count += 1
    
    return matrix


def test():
    answer = generateMatrix(5)
    for matrice in answer:
        print(matrice)


if __name__ == "__main__":
    test()