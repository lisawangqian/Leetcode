# """
# This is the interface that allows for creating nested lists.
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        numList = [0] * (num+1)
        
        for i in range(num + 1):
            numList[i] = sum(map(int, list(bin(i)[2:])))
            
        return numList