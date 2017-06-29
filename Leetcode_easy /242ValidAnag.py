class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dics = {}
    
        for c in s:
            if c in dics:
                dics[c] += 1
            else:
                dics[c] = 1
        for c in t:
            if not (c in dics):
                return False
            else:
                dics[c] -=1
                if dics[c] < 0:
                    return False
        for v in dics.values():
            if v != 0:
                return False
        
        return True
        