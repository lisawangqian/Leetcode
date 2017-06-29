class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ""
        while n > 0:
            n -=1
            s = chr(n%26+ord('A')) + s
            n = n/26
            
        return s        