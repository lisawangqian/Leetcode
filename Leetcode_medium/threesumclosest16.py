class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        if len(nums)<3:
            return None
        i=0
        diff=abs(nums[0]+nums[1]+nums[2]-target)
        result=nums[0]+nums[1]+nums[2]
        while i<len(nums)-2:
            left=i+1
            right=len(nums)-1
            while left < right:
                tem=nums[i]+nums[left]+nums[right]
                if tem==target: 
                    return target
                elif tem < target:
                    if target-tem<diff:
                        diff=target-tem
                        result=tem
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                else:
                    if tem-target<diff:
                        diff=tem-target
                        result=tem
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
            i+=1
            while i<len(nums)-2 and nums[i]==nums[i-1]:
                i+=1
        
        return result
                    
        
        
        