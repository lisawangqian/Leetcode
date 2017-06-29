class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n==0:
            return []
        res=[]
        self.dfs(n, n, res, "")
        return res
        
    def dfs(self, left, right, res, element):
        if left>right:
            return
        if left==0 and right==0:
            res.append(element)
        if left>0:
            self.dfs(left-1, right, res, element+"(")
        if right>left:
            self.dfs(left, right-1, res, element+")")