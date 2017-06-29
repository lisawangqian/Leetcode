'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

'''




class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
       
        group = {}
        
        for word in strings:
            #tuple can be dic key but list cannot
            shift = tuple((ord(word[i]) - ord(word[i-1])) % 26 for i in range(1,len(word)))
            if shift in group:
                group[shift].append(word)
            else:
                group[shift] = [word]
            
        
        return map(sorted, group.values())