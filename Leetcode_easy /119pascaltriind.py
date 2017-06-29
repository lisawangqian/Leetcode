'''
Given an index k, return the kth row of the Pascal's triangle.
'''



class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        preResult = [1]
        
        
        for i in range(1, rowIndex+1):
            subResult = [1]
            for j in range(i-1):
                 subResult.append(preResult[j] + preResult[j+1])
            subResult.append(1)
            preResult = subResult[:]
            
            
        return preResult