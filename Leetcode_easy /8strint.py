class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        nLen = len(str)
     
        while i < nLen and str[i].isspace():
            i+=1
        if i == nLen:
            return 0
            
        str = str[i:]
        
        flag = 1
        sign = 0
        
        if str[0] == "-":
            flag = -1
            str = str[1:]
            sign = 1
        elif str[0] == "+":
            str = str[1:]
            sign = 1
        
        if not str:
            return 0
        
        i = 0
        nLen = len(str)
     
        while i < nLen and str[i].isdigit():
            i+=1
            
        if not str[:i]:
            return 0
            
        new = int(str[:i])
        new = new * flag
        
        if new > 2147483647:
            return 2147483647 
        if new < -2147483648:
            return -2147483648
        
        return new
            