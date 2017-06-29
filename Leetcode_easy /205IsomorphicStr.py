'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

'''


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            if s[i] in dic1:
                dic1[s[i]].append(i)
            else:
                dic1[s[i]] = [i]
            if t[i] in dic2:
                dic2[t[i]].append(i)
            else:
                dic2[t[i]] = [i]
            
            if dic1[s[i]] != dic2[t[i]]:
                return False
        return True