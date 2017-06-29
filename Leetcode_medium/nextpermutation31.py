class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        l=len(nums)
        if l<=1: return 
        partion=l-1
        while partion>0 and nums[partion-1]>=nums[partion]:
            partion-=1
    
        if partion==0:
            nums.reverse()
        else:
            partion-=1
            new=l-1
            while new>0 and nums[new]<=nums[partion]:
                new-=1
            nums[partion], nums[new] = nums[new], nums[partion]
            tem=nums[partion+1:][::-1]
            nums[partion+1:]=tem
            
            
            
'''
STL中的经典算法。在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，然后将partition后的元素（不包括partition指向的元素）逆序排列。比如14532，那么升序对为45，partition指向4，由于partition之后除了5没有比4大的数，所以45交换为54，即15432，然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。

'''