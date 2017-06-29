class Solution:
    # @param {string} s
    # @return {string}
## http://www.felix021.com/blog/read.php?2040  
    def longestPalindrome(self, s):
        news="#"+"#".join(s)+"#"
        
        p = [1] * len(news)
        id, mx = 0, 1
        
        for i in range(1, len(news)):
            i_mirror=2*id-i
            if mx>i and p[i_mirror]< mx-i:
                    p[i]=p[i_mirror]
            else:
                    if mx>i:
                         p[i]=mx-i
                    else:
                         p[i]=1
                
                    while i+p[i]<len(news) and i>=p[i] and news[i+p[i]]==news[i-p[i]]:
                         p[i]+=1
                
                    if mx<p[i]+i:
                        id=i
                        mx=p[i]+i
    
        index, maxlen = 0, 0
        for i in range(0, len(news)):
            if p[i]>maxlen:
                maxlen=p[i]
                index=i
        
        result= news[index-maxlen+1: index+maxlen].replace("#","")
        return result
        
'''dp        
        
class Solution:
    # @param {string} s
    # @return {string}
  
    def longestPalindrome(self, s):
        l = len(s)  
        p=[[0 for i in range(l)] for j in range(l)]  
        maxL=0
        start=0
        end=0
        
        for i in range(l):
              for j in range(i):  
                    if i==j+1:
                        p[j][i]=(s[i]==s[j])
                    elif j+1<=i-1:
                        p[j][i]=(s[i] == s[j]) and p[j+1][i-1]
                    
                    if p[j][i] and maxL < (i-j+1): 
                              maxL = i-j+1  
                              start = j  
                              end = i  
              p[i][i] =1 
            
        return s[start:end+1]
'''