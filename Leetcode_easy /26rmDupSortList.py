'''
    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
    
    Do not allocate extra space for another array, you must do this in place with constant memory.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        n = len(nums)
        i = 1
        while i < n:
            if nums[i] == nums[i-1]:
                nums.pop(i)
                n -= 1
            else:
                i += 1
        return len(nums)