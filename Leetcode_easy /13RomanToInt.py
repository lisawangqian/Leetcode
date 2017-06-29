'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Hide Company Tags

'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} 
        s = s.upper()
        
        previous = ""
        cum = 0
        for c in s:
            cum += dic[c]
            if (c == "V" or c == "X") and (previous == "I"):
                cum -= 2
            if (c == "L" or c == "C") and (previous == "X"):
                cum -= 20
            if (c == "D" or c == "M") and (previous == "C"):
                cum -= 200
            previous = c
            
        return cum
            