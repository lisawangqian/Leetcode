'''
Given an integer, write a function to determine if it is a power of two.


'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <=0:
            return False
        s = bin(n)[2:]
        if len(s) == 1:
            return True
        for c in s[1:]:
            if c == "1":
                return False
        return True
        