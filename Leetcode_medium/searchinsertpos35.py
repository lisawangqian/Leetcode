class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1
        if target>nums[right]:
            return right+1
        if target<nums[left]:
            return left
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
                if nums[right]<target:
                    return mid
            elif nums[mid]<target:
                left=mid+1
                if nums[left]>target:
                    return left
            else:
                return mid