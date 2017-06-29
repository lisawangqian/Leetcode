class Solution(object):
    def isPalindrome(self, s):
        """
            :type s: str
            :rtype: bool
            """
        s =s.lower()
        s = s.split()
        s = "".join(s)
        
        i = 0
        n = len(s)-1
        while i<n:
            if not ("a" <= s[i] <= "z" or "0" <= s[i] <="9"):
                i+=1
            elif not ("a" <= s[n] <= "z" or "0" <= s[n] <="9"):
                n -=1
            else:
                if s[i] != s[n]:
                    return False
                else:
                    i+=1
                    n-=1
        return True

