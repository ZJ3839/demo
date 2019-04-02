class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x < 0:
            return -1
        if x<=1:
            return x
        l=1 
        r=x 
        res = 0
        while l<= r:
            mid = l + (r - l)//2
            if mid <= x//mid:
                res=mid
                l=mid+1 
            else :
                r = mid -1
        return res 
