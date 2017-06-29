'''
Given an integer n, return the number of trailing zeroes in n!.
'''


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        
        s = 0
        while n >= 5:
           s += n/5
           n = n/5
            
        return s    