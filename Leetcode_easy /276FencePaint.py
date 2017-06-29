class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        
        """
        if n == 0:
            return 0;
        if n < 2:
            return k
        """
        d[i] last two different color
        s[i] last two same color
        t[i] = d[i] + s[i]: no three adjacent same color
        """
        d = [0] * n
        s = [0] * n
        t = [0] * n
        d[0] = k
        d[1] = k * (k-1)
        s[0] = 0
        s[1] = k
        t[0] = k
        t[1] = k * k
        if n > 2:
           for i in range(2, n):
                s[i] = d[i-1]
                d[i] = (k-1) * d[i-1] + (k-1) * s[i-1]
                t[i] = s[i] + d[i]
        
        return t[n-1]
            
    
        
        