cclass Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split("."))
        v2 = map(int, version2.split("."))
        
        v1Len = len(v1)
        v2Len = len(v2)
        
        if v1Len > v2Len:
            v2 = v2 + [0] * (v1Len-v2Len)
        elif v1Len < v2Len:
            v1 = v1 + [0] * (v2Len-v1Len)
        
        newLen = max(v1Len, v2Len)
        i = 0
        
        while i < newLen and v1[i] == v2[i]:
            i+=1
        
        if i == newLen:
            return 0
        elif v1[i] > v2[i]:
            return 1
        else:
            return -1