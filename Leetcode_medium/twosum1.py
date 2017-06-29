class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dic={}
        n=len(nums)
        for i in range(n):
            x=nums[i]
            if (target-x) in dic:
                return (dic[target-x]+1, i+1)
            dic[x]=i