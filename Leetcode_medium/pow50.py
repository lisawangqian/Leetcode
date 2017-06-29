class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
         if n==0:
             return 1.0
         elif n<0:
             return 1/self.myPow(x, -n)
         elif n%2!=0:
             return self.myPow(x*x, n/2) * x
         else:
             return self.myPow(x*x, n/2) 