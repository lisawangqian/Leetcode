class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        if len(nums)<3:
            return []
        
        result=[]
        i=0
        
        while i < len(nums)-2:
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left]+nums[left+1]+nums[i] > 0 or nums[right]+nums[right-1]+nums[i] < 0:
                    break;
                if nums[left]+nums[right]+nums[i]==0:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif nums[left]+nums[right]+nums[i] < 0:
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                else:
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
            i+=1
            while i<len(nums)-2 and nums[i]==nums[i-1]:
                i+=1
                        
        return result