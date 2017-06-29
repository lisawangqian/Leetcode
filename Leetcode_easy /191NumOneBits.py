'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0
        s = bin(n)[2:]
        for c in s:
            ones += int(c)
        return ones