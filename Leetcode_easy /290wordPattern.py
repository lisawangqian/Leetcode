'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(str) != len(pattern):
            return False
        dicp ={}
        dics = {}
        for i in range(len(pattern)):
            if pattern[i] in dicp:
                dicp[pattern[i]].append(i)
            else:
                dicp[pattern[i]] = [i]
                
            if str[i] in dics:
                dics[str[i]].append(i)
            else:
                dics[str[i]] = [i]  
            if dics[str[i]] != dicp[pattern[i]]:
                return False
        return True