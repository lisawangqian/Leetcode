'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
'''




class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        cum = self.squaredigit(n)
        #or use set, set.add: as hashtable with key only
        dic = {cum: 0}
        while cum != 1:
            cum = self.squaredigit(cum)
            if not(cum in dic):
                dic[cum] = 0
            else:
                break;
        if cum == 1:
            return True
        else:
            return False
        
    def squaredigit(self, n):
        s = 0
        while n/10 != 0:
            digit = n%10
            s += digit * digit
            n = n/10
        s = s + n * n
        return s