class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        result=""
        ftable={1:"I", 5:"V", 10 :"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        k=list(ftable.keys())
        k.sort(reverse=True)
        m=0
        while num != 0:
            n = num // k[m]
            if n!=0:
                result += ftable[k[m]]*n
                num -= k[m] * n
            m+=1
           
            
        trans={"DCCCC": "CM", "CCCC": "CD", "LXXXX":"XC", "XXXX":"XL", "VIIII":"IX", "IIII":"IV"}
        tk=["DCCCC", "CCCC", "LXXXX", "XXXX", "VIIII", "IIII"]
        for word in tk:
            if word in result:
                result=result.replace(word, trans[word])
        return result
        
        