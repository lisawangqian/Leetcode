'''
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

'''
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        result=[]
        for i in range(n-1):
            if s[i]==s[i+1] and s[i]=="+":
                if i!=n-2:
                   result.append(s[:i] + "-" + "-" + s[i+2:])
                else:
                   result.append(s[:i] + "-" + "-")
        return result
                