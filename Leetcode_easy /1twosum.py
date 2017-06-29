class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
                
        for (key, val) in dic.iteritems():
            if target == 2*key:
                if len(val) == 2:
                    return val
            else:
                if (target-key) in dic:
                    return [val[0], dic[target-key][0]]
            