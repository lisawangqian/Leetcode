class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        sum=0
        maxsum=-10000
        for i in range(len(nums)):
            if sum<0:
                sum=0
            sum+=nums[i]
            maxsum=max(maxsum, sum)
            
        return maxsum