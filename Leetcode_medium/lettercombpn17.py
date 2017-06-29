class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
         
         def acc(start, string, output):
             if start==length:
                 output.append(string)
                 return
             for i in letter[digits[start]]:
                     acc(start+1, string+i, output)
         
         letter = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5": ["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
         
         if digits == "":
             return [ ]
         length=len(digits)
         output=[]
         acc(0, "", output)
         
         return output
             