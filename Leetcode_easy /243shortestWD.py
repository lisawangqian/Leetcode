'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
'''

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index = 0
        i = -1
        j = -1
        m = len(words)
        for word in words:
            if word == word1:
                i = index
            elif word == word2:
                j = index
            if i >=0 and j>=0 and (abs(i-j)) < m :
                m = abs(i-j)
            index += 1
            
        return m
       