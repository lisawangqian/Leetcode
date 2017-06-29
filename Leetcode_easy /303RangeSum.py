'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

'''



class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.data = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            self.data.append(s)
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.data[j]
        else:
            return self.data[j] -self.data[i-1]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)