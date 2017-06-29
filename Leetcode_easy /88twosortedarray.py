'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

'''



class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        length = m + n
        i = 0
        j = 0
        if n == 0:
            return
        while i < length:
            if j < n:
               if (i < m) and (nums1[i] <= nums2[j]):
                   i += 1
               else:
                   nums1.pop()
                   nums1.insert(i,nums2[j])
                   j += 1
                   i += 1 
                   m += 1
            else:
                return
            