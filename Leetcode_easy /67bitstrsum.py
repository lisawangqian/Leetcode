'''
Given two binary strings, return their sum (also a binary string).
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    
        c = [0]
        
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        if len(b) > len(a):
            a = "0" * (len(b) - len(a)) + a
            
        for i in range(max(len(a), len(b))):
            c.append(int(b[i]) + int(a[i]))
            
        n = len(c) - 1
        while n > 0:
            if c[n] >= 2:
                c[n-1] = c[n-1] + c[n]/2
                c[n] = c[n] % 2
                
                n = n-1
            else:
                n = n-1
                
        if c[0] == 0:
            c.pop(0)
        
        return "".join(map(str, c))
            
            