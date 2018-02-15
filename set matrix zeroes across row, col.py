"""

class Solution(object):
    def setZeroes(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 1 and matrix[i][j] > -1:
                    r = 0
                    while (r < len(matrix)):
                        matrix[r][j] = float(matrix[r][j])
                        r += 1
                    c = 0
                    while (c < len(matrix[0])):
                        matrix[i][c] = float(matrix[i][c])
                        c += 1
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if isinstance(matrix[x][y],float):
                    matrix[x][y] = 0

"""