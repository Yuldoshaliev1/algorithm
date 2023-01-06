#https://leetcode.com/problems/toeplitz-matrix/

matrix = [[1,2],[2,2]]

print( all(matrix[i][j] == matrix[i - 1][j - 1] for i in range(1, len(matrix)) for j in range(1, len(matrix[0]))))
