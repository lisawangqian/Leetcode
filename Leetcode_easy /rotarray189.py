class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        n=len(nums)
        index=n-k
        nums[:]=nums[index:]+nums[:index]
        
        
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        
        if len(nums)>=k:
            lst=[]
            for i in range(len(nums)-k,len(nums)):
                 lst.append(nums[i])
            for i in range(len(nums)-k):
                 lst.append(nums[i])
        
        nums[:]=lst
        
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
          for i in range(k):
              num=nums.pop()
              nums.insert(0,num)
             
'''