class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    
    def dfs(self, candidates, target, start, valuelst):
        l=len(candidates)
        if target==0:
            self.result.append(valuelst)
            return
        for i in range(start,l):
            if candidates[i]>target:
                return
            self.dfs(candidates, target-candidates[i], i, valuelst+[candidates[i]])
    
    
    def combinationSum(self, candidates, target):
        
        candidates.sort()
        self.result=[]
        self.dfs(candidates, target, 0, [])
        return self.result
        