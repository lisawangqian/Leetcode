class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        left, right = 0, len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                res=[0,0]
                if nums[right]==target:
                    res[1]=right
                else:
                    i=mid+1
                    while i<right and nums[i]==target:
                        i+=1
                    res[1]=i-1
                if nums[left]==target: 
                    res[0]=left
                else:
                    i=mid-1
                    while i>left and nums[i]==target:
                        i-=1
                    res[0]=i+1
                return res
                
        return [-1, -1]