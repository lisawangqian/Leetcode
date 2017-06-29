'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while (num/10) != 0:
            num = sum([int(c) for c in str(num)])
        return num
        '''       
        if num == 0:
            return 0
        elif num%9 == 0:
            return 9
        else:
            return num%9  
        '''      