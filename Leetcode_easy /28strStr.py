'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nl = len(needle)
        
        hl = len(haystack)
        
        if nl > hl :
            return -1
            
        for i in range(hl-nl+1):
            if haystack[i: i+ nl] == needle:
                return i
            
        return -1    