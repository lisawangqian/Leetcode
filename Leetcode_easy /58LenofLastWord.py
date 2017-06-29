'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.


'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        s = s[::-1]
        
        i = 0
        while i < len(s) and s[i] == " ":
            i+=1
            
        if i == len(s): 
            return 0
        else:
            j = i
            while j < len(s) and s[j] != " ":
                j+=1
                
        return j-i
        
        
    '''
    
    def lengthOfLastWord(self, s):
        s=s.split()
        if len(s)==0:
            return 0
        return len(s[-1])
    
    '''