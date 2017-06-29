'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n <= 0:
            return ""
        if n == 1:
            return "1"
            
        collect = ["1", "11"]
        
        for i in range(2, n):
            previous = collect[i-1]
            index = []
            count = 1
            m = 1
            l = len(previous)
            while m < l:
                if previous[m] == previous[m-1]:
                    count +=1
                    m += 1
                else:
                    index.append([previous[m-1],count])
                    count = 1
                    m += 1
                
            index.append([previous[m-1],count])     
                
            
            s = ""
            for value in index:
                s += str(value[1]) + value[0]
            
            collect.append(s)
        
        return collect[n-1]
                    
            