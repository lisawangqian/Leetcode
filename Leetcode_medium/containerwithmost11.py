class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        areamax = 0
        left, right = 0, len(height)-1
        while left<right:
            areamax=max(areamax, (right-left)*min(height[left], height[right]))
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1
        return areamax