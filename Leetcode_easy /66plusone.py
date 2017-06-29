'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        digits[n-1] = digits[n-1] + 1
        i = n-1
        while i > 0 and digits[i] > 9:
            d1 = digits[i]%10
            d2 = digits[i]/10
            digits[i] = d1
            digits[i-1] = digits[i-1] + d2
            i -= 1
        
        if digits[0] > 9: 
            d1 = digits[0]%10
            d2 = digits[0]/10
            digits[0] = d1
            digits.insert(0, d2)
        
        return digits
            
            