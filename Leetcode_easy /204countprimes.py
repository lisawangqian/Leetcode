'''
Count the number of prime numbers less than a non-negative number, n.

'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
            
        isPrime = [0] *2 + [1] * (n-2)
        
        p = 2
        while p*p < n:
            if isPrime[p] == 1: 
               j = p*p
               while j < n:
                   isPrime[j] = 0
                   j+=p
            
            p+=1
            
        return sum(isPrime)