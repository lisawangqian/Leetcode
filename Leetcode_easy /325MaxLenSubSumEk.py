'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
'''


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if (not nums) or len(nums) == 0:
            return 0
            
        n = len(nums)
        maxLen = 0
        dic = {0:-1}
        cum = 0
        for i in range(n):
           cum += nums[i] 
           if not (cum in dic):
               dic[cum] = i
           if (cum - k) in dic:
               maxLen = max(maxLen, i - dic[cum-k])
            
        return maxLen
            