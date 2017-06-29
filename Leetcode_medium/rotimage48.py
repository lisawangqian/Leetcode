class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        
        length=len(matrix)
        
        for i in range(length-1):
            for j in range(i+1, length):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
                
        for i in range(length):
            matrix[i].reverse()
            