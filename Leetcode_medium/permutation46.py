class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    
    def permute(self, nums):
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [nums]
        res=[]
        for i in range(len(nums)):
            for j in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+j)
        
        return res
        
        