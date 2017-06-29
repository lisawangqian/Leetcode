'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = "()"
        s2 = "[]"
        s3 = "{}"
        
        while (s1 in s) or (s2 in s) or (s3 in s):
            if s1 in s:
                s = s.replace(s1, "")
            if s2 in s:
                s = s.replace(s2, "")
            if s3 in s:
                s = s.replace(s3, "")
                
        if len(s) == 0:
            return True
        else:
            return False