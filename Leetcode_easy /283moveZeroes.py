'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        i = 0
        
        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                n -= 1
            else:
                i += 1
            
            
       