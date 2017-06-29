class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums)<4:
            return []
        dic={}
        s=set()
        nums.sort()
        for p in range(len(nums)-1):
            for q in range(p+1, len(nums)):
                if nums[p]+nums[q] not in dic:
                     dic[nums[p]+nums[q]]=[(p,q)]
                else:
                     dic[nums[p]+nums[q]].append((p,q))
        
        for p in range(len(nums)-3):
            for q in range(p+1, len(nums)-2):
                if target-nums[p]-nums[q] in dic:
                    for i in dic[target-nums[p]-nums[q]]:
                        if i[0]>q:
                            s.add((nums[p], nums[q], nums[i[0]], nums[i[1]]))
            
                
        return [list(i) for i in s]