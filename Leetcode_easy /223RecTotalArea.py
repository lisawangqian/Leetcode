'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

'''


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if C <= E or G <= A or B >= H or F >= D:
            sub = 0
        else:
            if A <= E:
                x1 = E
            else:
                x1 = A
        
            if C <= G:
                x2 = C
            else:
                x2 = G
        
            x = x2-x1
        
            if D <= H:
                y2 = D
            else:
                y2 = H
        
            if B <= F:
                y1 = F
            else:
                y1 = B
        
            y = y2 -y1
        
            sub = y*x
        
        return (C-A)*(D-B) + (G-E)*(H-F) - sub
            