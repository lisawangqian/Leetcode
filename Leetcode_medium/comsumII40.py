class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    
    def dfs(self, candidates, target, start, valuelst):
        l=len(candidates)
        if target==0:
            if valuelst not in self.result:
                   self.result.append(valuelst)
            return
        for i in range(start,l):
            if candidates[i]>target:
                return
            self.dfs(candidates, target-candidates[i], i+1, valuelst+[candidates[i]])
    
    
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.result=[]
        self.dfs(candidates, target, 0, [])
        return self.result