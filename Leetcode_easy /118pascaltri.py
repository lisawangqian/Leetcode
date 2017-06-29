'''
Given numRows, generate the first numRows of Pascal's triangle.
'''






class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        preResult = [1]
        result = [[1]]
        
        for i in range(1, numRows):
            subResult = [1]
            for j in range(i-1):
                 subResult.append(preResult[j] + preResult[j+1])
            subResult.append(1)
            result.append(subResult)
            preResult = subResult[:]
            
            
        return result
        