'''
Given a string, determine if a permutation of the string could form a palindrome.
'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) == 1:
            return True
            
        table = {}
        for c in s:
            if c in table.keys():
                table[c] += 1
            else:
                table[c] = 1
        
        count = 0
        for value in table.values():
            if value % 2 == 1:
                count +=1
            if count > 1:
                return False
        
        return True    
                
        