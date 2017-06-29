
'''
Reverse bits of a given 32 bits unsigned integer.
'''



class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]
        s= s[::-1] + (32-len(s)) * "0"
        
        return int(s,2)