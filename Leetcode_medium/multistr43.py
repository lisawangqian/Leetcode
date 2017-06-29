class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    
    
    
    def multiply(self, num1, num2):
        num1=num1[::-1]
        num2=num2[::-1]
        arr=[0 for i in range(len(num1)+len(num2))]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j]+=int(num1[i])*int(num2[j])
        s=[]
        for i in range(len(arr)):
            cur=arr[i]%10
            nex=arr[i]/10
            if i<len(arr)-1:
               arr[i+1]+=nex
            s.insert(0, str(cur))
    
        while s[0]=="0" and len(s)>1:
            del s[0]
        return "".join(s)