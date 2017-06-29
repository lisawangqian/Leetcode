class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        old = x
        compare = 0
        while x/10 > 0:
            compare = compare*10 + x%10
            x = x/10
        compare = compare*10 + x
        
        return compare == old
        
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
            
        new = str(x)
        compare = new[::-1]
        
        return new == compare

'''