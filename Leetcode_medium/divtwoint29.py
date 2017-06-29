class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        sum, count, res = 0, 0, 0
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
           
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = - res
        if res>2147483647:
                res=2147483647
        if res<-2147483648:
                res=-2147483648
        return res
            