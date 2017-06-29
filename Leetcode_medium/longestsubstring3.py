class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        
        dic={}
        for i in range(len(s)):
            dic[s[i]]=-1
        
        st=0
        maxl=0
        for i in range(len(s)):
            if dic[s[i]]!=-1:
                while st<=dic[s[i]]:
                    dic[s[st]]=-1
                    st+=1
            if maxl < i-(st-1):    #need to be outside first if, need to increase maxl until meet a repeat.
                maxl = i-(st-1)
                
            dic[s[i]]=i
        return maxl