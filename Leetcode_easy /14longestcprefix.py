'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        longest = strs[0]
       
        i = 1
        for current in strs[1:]:
            l1 = len(longest)
            l2 = len(current)
            j = 0
            while j < l1 and j < l2 and current[j] == longest[j]:
                j+=1
            longest = current[:j]
        
        return longest