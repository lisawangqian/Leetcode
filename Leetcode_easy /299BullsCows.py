
'''
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
'''



class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dic = {}
        a = 0
        b = 0
        index = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a+=1
            else:
                index.append(i)
                if (not secret[i] in dic):
                    dic[secret[i]] = 1
                else:
                    dic[secret[i]] += 1
        for i in index:
            if (guess[i] in dic) and (dic[guess[i]] > 0):
                b+=1
                dic[guess[i]] -= 1
        
                    
        return str(a) + "A" + str(b) + "B"
                    
            