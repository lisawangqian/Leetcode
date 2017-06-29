# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buff4 = [""] * 4
        ncRead = 0
        end = False
        while ncRead < n and (not end):
            count = read4(buff4)
            if count != 4:
                end = True
            m = min(count, n-ncRead)
            for i in range(m):
                buf[ncRead] = buff4[i];
                ncRead+=1
                
        return ncRead
                