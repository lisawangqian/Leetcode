'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''



class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        elif n <= 2:
            return n
            
        way = [0] * n
        way[0] = 1
        way[1] = 2
        for i in range(2, n):
            way[i] = way[i-1] + way[i-2]
        return way[n-1]