'''
Given a sorted integer array without duplicates, return the summary of its ranges.

'''




class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        i = 1
        start = 0
        index = []
        while i < len(nums):
            if nums[i] == nums[i-1] + 1:
                i+=1
            else:
                index.append([start, i-1])
                start = i
                i+=1
        index.append([start, i-1])
        
        result = []
        for (s, e) in index:
            if s == e:
                result.append(str(nums[s]))
            else:
                result.append(str(nums[s]) + "->" + str(nums[e]))
        return result
            