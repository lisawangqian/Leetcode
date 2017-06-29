'''
Given an integer, write a function to determine if it is a power of three
'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 0:
            return False
            
        while n%3 == 0:
            n = n/3
    
        return n == 1
        