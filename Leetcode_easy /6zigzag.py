
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

'''



class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        nLen = len(s)
        
        result = [""] * numRows
        
        i = 0
        pos = -1
        direct = 1
        while i < nLen:
            pos += direct
            if pos == numRows:
                pos -= 2
                direct = -1
            elif pos == -1:
                pos = 1
                direct = 1
                
            result[pos] += s[i]
            i += 1
            
        return "".join(result)
                