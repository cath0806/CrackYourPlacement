class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        area=0
        a=0
        i=0
        j=n-1
        while(j>i):
            d=j-i
            if(height[i]<height[j]):
                a=height[i]*d
                i=i+1
            else:
                a=height[j]*d
                j=j-1
            if(area<a):
                area=a
        return area
