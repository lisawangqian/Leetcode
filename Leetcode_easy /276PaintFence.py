'''
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.
'''


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        
        posts = [0] * n
        
        posts[0] = k
        posts[1] = k*k
        
        for i in range(2, n):
            posts[i] = posts[i-2] * (k-1) + posts[i-1] * (k-1)
        
        return posts[-1]