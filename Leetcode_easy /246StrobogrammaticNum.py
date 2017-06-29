'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {"6":"9", "9":"6", "1":"1", "8":"8", "0":"0" }
        
        
        while len(num) >= 1:
            if not(num[0] in dic):
                return False
            elif dic[num[0]] != num[-1]:
                return False
            else:
                num = num[1:-1]
        
        return True 