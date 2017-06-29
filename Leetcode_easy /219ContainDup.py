'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

'''



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                for value in dic[nums[i]]:
                    if abs(i - value) <= k:
                        return True
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
            
        return False           
            