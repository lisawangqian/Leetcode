class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
       dic={}
       for str in strs:
           str2="".join(sorted(str))
           if str2 not in dic:
               dic[str2]=[str]
           else:
               dic[str2].append(str)
       result=[]
       
       for key, value in dic.items():
           if len(value) >= 2:
               for ana in value:
                   result.append(ana)
       return result