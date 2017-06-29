class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1
            x = abs(x)
        x = str(x)
        x = x[::-1]
        x = int(x)
        
        if flag>0:
            if x > 2147483647:
                return 0
        else:
            if x > 2147483648:
                return 0
        
        return flag * x
        